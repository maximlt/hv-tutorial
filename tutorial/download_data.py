import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import zipfile


files_to_download = [
    {
        "url": "https://datasets.holoviz.org/population/v1/gpw_v4_population_density_rev11_2010_2pt5_min.zip",
        "description": "Population Raster",
        "filename": "raster.zip",
    },
    {
        "url": "https://datasets.holoviz.org/earthquakes/v1/earthquakes-projected.parq",
        "description": "Earthquakes",
        "filename": "earthquakes-projected.parq"
    },
]

SCRIPT_DIR = Path(__file__).parent


def download_file(file_info: dict[str, str]):
    """Download a file from a URL to a specified output path."""
    url = file_info["url"]
    output_path = SCRIPT_DIR / "data" / file_info["filename"]
    description = file_info["description"]

    # Check if the file already exists
    if output_path.exists() or (output_path.suffix == ".zip" and output_path.with_suffix('').exists()):
        print(f"File already exists: {output_path}. Skipping download.")
        return

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'wb') as file, tqdm(
        desc=f"Downloading {description}",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            bar.update(len(data))
    print(f"Downloaded {description} to: {output_path}")

    if output_path.suffix == '.zip':
        unzip_file(output_path)
        output_path.unlink()

def unzip_file(zip_path: Path):
    """Unzip a .zip file to the same directory."""
    extract_dir = zip_path.with_suffix('')
    print(f"Unzipping {zip_path} to {extract_dir}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Unzipped {zip_path} to {extract_dir}")

def main():
    with ThreadPoolExecutor() as executor:
        futures = executor.map(download_file, files_to_download)
        try:
            # Explicitly iterate over the results to catch exceptions
            for _ in futures:
                pass
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

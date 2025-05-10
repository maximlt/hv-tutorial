from pathlib import Path
import zipfile

ARCHIVE_NAME = 'holoviz_tutorial.zip'

def create_zip(output_filename, base_dir):
    base_dir = Path(base_dir)
    output_filename = Path(output_filename)

    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        files = ['pixi.toml', 'pixi.lock']
        for file in files:
            pixi_toml_path = base_dir / file
            zipf.write(pixi_toml_path, arcname=file)
        tutorial_dir = base_dir / 'tutorial'
        for file_path in tutorial_dir.rglob('*'):
            if file_path.name == 'conf.py':
                continue
            if any(d in file_path.parts for d in ['data', '.ipynb_checkpoints', '__pycache__']):
                continue
            arcname = file_path.relative_to(base_dir)
            zipf.write(file_path, arcname=arcname)

if __name__ == "__main__":
    base_directory = Path(__file__).parent.parent
    output_zip = base_directory / ARCHIVE_NAME
    create_zip(output_zip, base_directory)
    print(f"Created zip file: {output_zip}")

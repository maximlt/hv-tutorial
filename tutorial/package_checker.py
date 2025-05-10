import tomllib
import pathlib
import sys
from packaging.version import Version

def get_required_versions(toml_path):
    """
    Reads the pixi.toml configuration and extracts all package version requirements.
    
    Args:
        toml_path (str): Path to the pixi.toml file.
    
    Returns:
        dict: A dictionary mapping package names to their required versions.
    """
    toml_file_path = pathlib.Path(toml_path)
    with open(toml_file_path, 'rb') as file:
        data = tomllib.load(file)
        dependencies = data.get('dependencies', {})
        version_dict = {}
        for package, version in dependencies.items():
            # Handle cases where version constraints are specified
            if isinstance(version, str):
                for delimiter in ['==', '>=']:
                    if delimiter in version:
                        version = version.split(delimiter)[1].split(',')[0]
                        version_dict[package] = version
                        break
                else:
                    # If no delimiter is found, assume exact version
                    version_dict[package] = version
            else:
                # If version is not a string, assume no version constraint
                version_dict[package] = None
        return version_dict

def check_packages(packages, toml_path='../pixi.toml'):
    """
    Checks if specified packages are installed with correct versions as per the pixi.toml configuration.
    
    Args:
        packages (list): A list of package names to check.
        toml_path (str): Path to the pixi.toml file.
    """
    required_versions = get_required_versions(toml_path)
    error_found = False
    for pkg in packages:
        try:
            req_version = required_versions.get(pkg)
            installed_version = sys.modules[pkg].__version__
            if req_version and Version(installed_version) < Version(req_version):
                print(f"Error: {pkg} expected version {req_version}, got {installed_version}")
                error_found = True
        except KeyError:
            print(f"{pkg} is not installed or not specified in the TOML configuration.")
            error_found = True

    if not error_found:
        print("All specified packages are correctly installed.")

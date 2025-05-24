import requests

BASE_URL = "https://api.nasa.gov/mars-photos/api/v1"
DEMO_KEY = "DEMO_KEY"
api_key = DEMO_KEY

def get_photos_by_sol( rover, sol, camera=None):
    """
    Obtiene fotos por sol marciano.
    :param rover: Nombre del rover (curiosity, opportunity, spirit, perseverance)
    :param sol: Día marciano (int)
    :param camera: (opcional) Abreviatura de la cámara
    :return: JSON con las fotos
    """
    params = {"api_key": api_key, "sol": sol}
    if camera:
        params["camera"] = camera
    url = f"{BASE_URL}/rovers/{rover}/photos"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_photos_by_earth_date( rover, earth_date, camera=None):
    """
    Obtiene fotos por fecha terrestre.
    :param rover: Nombre del rover
    :param earth_date: Fecha en formato 'YYYY-MM-DD'
    :param camera: (opcional) Abreviatura de la cámara
    :return: JSON con las fotos
    """
    params = {"api_key": api_key, "earth_date": earth_date}
    if camera:
        params["camera"] = camera
    url = f"{BASE_URL}/rovers/{rover}/photos"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_latest_photos( rover):
    """
    Obtiene las fotos más recientes de un rover.
    :param rover: Nombre del rover
    :return: JSON con las fotos más recientes
    """
    params = {"api_key": api_key}
    url = f"{BASE_URL}/rovers/{rover}/latest_photos"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_manifest( rover):
    """
    Obtiene el manifiesto de la misión de un rover.
    :param rover: Nombre del rover
    :return: JSON con el manifiesto
    """
    params = {"api_key": api_key}
    url = f"{BASE_URL}/manifests/{rover}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
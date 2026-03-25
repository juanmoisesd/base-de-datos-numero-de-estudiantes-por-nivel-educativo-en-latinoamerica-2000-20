"""Base de datos sobre el n&uacute;mero de estudiantes seg&uacute;n nivel educativo
DOI:https://juanmoisesd.github.io/base-de-datos-numero-de-estudiantes-por-nivel-educativo-en-latinoamerica-2000-20/"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://juanmoisesd.github.io/base-de-datos-numero-de-estudiantes-por-nivel-educativo-en-latinoamerica-2000-20/".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Base de datos sobre el n&uacute;mero de estudiantes seg&uacu"
def info():print("DOI: https://juanmoisesd.github.io/base-de-datos-numero-de-estudiantes-por-nivel-educativo-en-latinoamerica-2000-20/\nGitHub: https://github.com/juanmoisesd/base-de-datos-numero-de-estudiantes-por-nivel-educativo-en-latinoamerica-2000-20")

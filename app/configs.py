from pathlib import Path
from typing import Dict, Any, List, Optional

import mlflow
import mlflow.pyfunc


# =========================
# MLflow Config
# =========================

MLFLOW_URI = "https://omarelrayes-mlflow-server.hf.space"

mlflow.set_tracking_uri(MLFLOW_URI)


# =========================
# Model Run IDs
# =========================

CLASSIFICATION_MODEL_URI = (
    "runs:/8cae153bb747447b9f9afa237470e00f/model"
)

SEGMENTATION_MODEL_URI = (
    "runs:/49dba7de7bb04aac851201051a497bf4/model"
)


# =========================
# Lazy Models
# =========================

_classification_model: Optional[mlflow.pyfunc.PyFuncModel] = None

_segmentation_model: Optional[mlflow.pyfunc.PyFuncModel] = None



def get_classification_model():

    global _classification_model

    if _classification_model is None:

        print(
            "Loading Classification Model........................\n############"
        )

        _classification_model = mlflow.pyfunc.load_model(
            CLASSIFICATION_MODEL_URI
        )

    return _classification_model



def get_segmentation_model():

    global _segmentation_model

    if _segmentation_model is None:

        print(
            "Loading Segmentation Model........................\n############"
        )

        _segmentation_model = mlflow.pyfunc.load_model(
            SEGMENTATION_MODEL_URI
        )

    return _segmentation_model



# =========================
# Metadata
# =========================

model_classes: Dict[int, str] = {

    0: "benign",
    1: "malicious"

}


request_history: List[Dict[str, Any]] = []



# =========================
# Storage
# =========================

STORAGE_DIR = Path("storage")

IMAGES_DIR = STORAGE_DIR / "images"

SEGMENTS_DIR = STORAGE_DIR / "segments"



for dir_path in [
    STORAGE_DIR,
    IMAGES_DIR,
    SEGMENTS_DIR
]:

    dir_path.mkdir(
        parents=True,
        exist_ok=True
    )

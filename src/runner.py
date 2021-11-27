import os
from .utils import load_model, load_data_from_file
from .infer import execute_inference
from .constants import output_file_name


def run(project_dir, model1_path: str, model2_path: str, data_path: str) -> str:
    """
    Function to run the inference process using file paths. This function takes the file paths to models and data
    and writes a output file with the results. It also returns the path to the file it has written.

    :param project_dir: The directory where all the model and data files are. Output file with be written here
    :param model1_path: Path to model 1
    :param model2_path: Path to model 2
    :param data_path: Path to the data file
    """

    model1 = load_model(os.path.join(project_dir, model1_path))
    model2 = load_model(os.path.join(project_dir, model2_path))
    data = load_data_from_file(os.path.join(project_dir, data_path))

    results = execute_inference(model1, model2, data)

    output_path = os.path.join(project_dir, output_file_name)
    with open(output_path, 'w') as f:
        f.write("\n".join(results))

    return output_path

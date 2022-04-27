import json
import pathlib


def get_project_dir():
	""" Input:
			None
		Output:
			project_dir: pathlib.Path - the path
				of the project directory
	"""
	this_file_path = pathlib.Path(__file__)
	project_dir = this_file_path.parents[1]
	return project_dir

def main():
	""" Loads a json document containing ascii representations of
	dogs. It then prints these dogs to stdout, because dogs are important.
	"""
	project_dir = get_project_dir()
	json_path = project_dir.joinpath('data').joinpath('dog.json')
	with open(json_path) as f:
		dog_json = json.load(f)
	for dog in dog_json['dogs']:
		print(dog)

if __name__ == "__main__":
	main()

import os
import yaml
import Ingest
import Report
import Clean

def load_yaml_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def execute_from_yaml(file_path):
    config = load_yaml_config(file_path)
    client = Ingest.CoinGeckoClient(api_key=os.getenv(config['ingest']['api_key_env_var_name']), version=config['ingest']['version'])
    data = client.query_endpoint(
        endpoint=config['ingest']['endpoint'],
        path_params={"ids": ",".join(config['ingest']['path_dict']['ids'])},
        query_params=config['ingest']['param_dict']
    )
    return data

if __name__ == "__main__":
    config_file = "config.yml"
    config = load_yaml_config(config_file)
    data = execute_from_yaml(config_file)

    save_path = config['ingest']['save_path']
    os.makedirs(save_path, exist_ok=True)
    with open(os.path.join(save_path, "data.json"), "w") as f:
        f.write(str(data))
    
    Clean.process_raw_data(save_path, config['ingest']['clean_path'])
    Report.generate_report(config['ingest']['clean_path'], config['ingest']['report']['report_path'],config['ingest']['report']['query'])
    
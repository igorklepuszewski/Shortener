import os


def export_envs(filepath):
    with open(filepath) as env_file:
        for line in env_file:
            line = line.strip()
            separatorIndex = line.find('=')
            env_name = line[:separatorIndex].strip()
            env_value = line[separatorIndex + 1:].strip()
            os.environ[env_name] = env_value

import subprocess
import paramiko
from app.core.config import CONFIGS


# Using subprocess to delegate NAO interactions to Python 2.7 scripts
def call_nao_script(script_name, *args):
    """
    Generic function to call a Python 2.7 script for NAO.
    :param script_name: The script path (e.g., "scripts/nao_interface.py")
    :param args: Arguments to pass to the script
    :return: Output from the script
    """
    python2_path = CONFIGS["PYTHON2_EXECUTABLE"]
    script_path = f"scripts/{script_name}"

    command = [python2_path, script_path] + list(map(str, args))

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        raise Exception(f"NAO script error: {result.stderr}")


def say_text(text):
    """
    Delegate text-to-speech functionality to a Python 2.7 script.
    """
    return call_nao_script("say_text.py", CONFIGS['IP'], CONFIGS['PORT'], text)


def record_audio():
    """
    Delegate audio recording to a Python 2.7 script.
    """
    return call_nao_script(
        "record_audio.py",
        CONFIGS['IP'],
        CONFIGS['PORT'],
        CONFIGS['soundRecordPath'],
        CONFIGS['AUDIO_FILE_TYPE'],
        CONFIGS['SAMPLING_FREQUENCY']
    )


def fetch_audio():
    """
    Fetch the recorded audio from the NAO robot using SSH.
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=CONFIGS['IP'],
        port=CONFIGS['DrivePORT'],
        username=CONFIGS['USER'],
        password=CONFIGS['PASS']
    )
    ftp_client = ssh_client.open_sftp()
    ftp_client.get(CONFIGS['soundRecordPath'], CONFIGS['localPath'])
    ftp_client.close()
    ssh_client.close()
    return f"Audio file saved to {CONFIGS['localPath']}"


def close_hand():
    """
    Delegate hand-closing functionality to a Python 2.7 script.
    """
    return call_nao_script("nao_interface.py", CONFIGS['IP'], CONFIGS['PORT'], "RHand")

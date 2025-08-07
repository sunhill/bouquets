import subprocess
import sys
import os

def test_cli_app():
    script_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'main.py')
    bouquet_data = []
    bouquet_data.append("AS2a2b3")
    bouquet_data.append("BL2a2")
    bouquet_data.append("")  # Add an empty line to simulate multiple lines input
    flower_data = []
    flower_data.append("aL")
    flower_data.append("bS")
    flower_data.append("aS")
    flower_data.append("bS")
    flower_data.append("aS")
    flower_data.append("aL")
    flower_data.append("aS")
    flower_data.append("bS")
    input_data = "\n".join(bouquet_data) + "\n" + "\n".join(flower_data) + "\n"
    print(f"Input data for the script:{input_data}")
    expected_output = []
    expected_output.append("AS1a2b")
    expected_output.append("BL2a")
    expected_output.append("AS2a1b")

    result = subprocess.run(
        [sys.executable, script_path],
        input=input_data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True
    )

    # print("STDOUT:", result.stdout.decode())
    # print("STDERR:", result.stderr.decode())
    assert result.returncode == 0  # Optional: check exit code

    output = result.stdout.decode()
    for expected in expected_output:
        assert expected in output


if __name__ == "__main__":
    test_cli_app()
    print("All tests passed!")
import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    detach=True,
    ports={"5000/tcp": 5051},
    security_opt=["apparmor=my-apparmor-profile"],
)
print(f"Container started: {container.short_id}")

exit_code, output = container.exec_run("cat /etc/passwd")
print(f"Attempt to read /etc/passwd: Exit Code {exit_code}, Output: {output.decode().strip()}")

exit_code, output = container.exec_run("/bin/bash -c 'echo bash-ran'")
print(f"Attempt to execute /bin/bash: Exit Code {exit_code}, Output: {output.decode().strip()}")

container.stop()
container.remove()

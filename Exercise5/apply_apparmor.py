import docker

client = docker.from_env()

print("Building image from Dockerfile...")
client.images.build(path=".", tag="flask-apparmor")

print("Running container with AppArmor profile...")
container = client.containers.run(
    "flask-apparmor",
    detach=True,
    ports={"5000/tcp": 5050},
    security_opt=["apparmor=my-apparmor-profile"],
)
print(f"Container started: {container.short_id}")

print("Inspecting container to verify AppArmor profile...")
info = client.api.inspect_container(container.id)
print("AppArmor profile applied:", info["HostConfig"]["SecurityOpt"])

print("Stopping the container...")
container.stop()
container.remove()

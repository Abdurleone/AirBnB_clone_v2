#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["34.207.121.60", "100.25.164.228"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True
    """
    if not os.path.isfile(archive_path):
        abort("Error: Archive file not found.")

    archive_name = os.path.basename(archive_path).split(".")[0]

    try:
        put(archive_path, "/tmp/")
        run("rm -rf /data/web_static/releases/{}/".format(archive_name))
        run("mkdir -p /data/web_static/releases/{}/".format(archive_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_name, archive_name))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_name, archive_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_name))
        return True
    except Exception as e:
        abort("Deployment failed: {}".format(str(e)))

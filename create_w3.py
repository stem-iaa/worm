import os
import grp
import pwd

W3_GROUP = "w3"


def get_groups(user):
    groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
    gid = pwd.getpwnam(user).pw_gid
    groups.append(grp.getgrgid(gid).gr_name)
    return groups


if __name__ == '__main__':
    for user in pwd.getpwall():
        user = user[0]
        if W3_GROUP not in get_groups(user):
            continue

        uwsgi_settings = {
            "vhost": "true",
            "socket": "/tmp/flask_socks/" + user + ".sock",
            "chdir": "/home/" + user + "/www/flask",
            "module": "app",
            "callable": "app",
            "mount": "/=app.py",
            "manage-script-name": "true",
            "plugins": "python3",
            "pythonpath": "python3",
            "py-autoreload": "3",
            "touch-reload": "/home/" + user + "/www/flask_reload"
        }

        uwsgi_available_path = "/etc/uwsgi/apps-available/flask_" + user + ".ini"
        if not os.path.exists(uwsgi_available_path):
            uwsgi_file = open(uwsgi_available_path, "w")
            uwsgi_file.write("[uwsgi]\n")
            for key in uwsgi_settings:
                uwsgi_file.write(key + " = " + uwsgi_settings[key] + "\n")
            uwsgi_file.close()

        uwsgi_enabled_path = "/etc/uwsgi/apps-enabled/flask_" + user + ".ini"
        if not os.path.exists(uwsgi_enabled_path):
            os.symlink(uwsgi_available_path, uwsgi_enabled_path)

        sock_path = "/tmp/flask_socks/" + user + ".sock"
        if not os.path.exists(sock_path):
            open(sock_path, "w").close()

    os.system("")

import os
import config
path = os.path.join(config.WORK_DIR, "{user_id}", "{solution_id}", "code")

gcc = gpp = ["%s/main" % (path), ]

java = "java -cp %s Main" % (path)

python3 = "python3 %s" % (os.path.join(path, "__pycache__", "main.cpython-310.pyc"))

Language = {
    "gcc": gcc,

    "g++": gpp,

    "java": java,

    "python2": '',

    "python3": python3,
}
Language_rm = {
    "gcc": gcc[0],

    "g++": gpp[0],

    "java": java.split()[2] + "/Main.class",

    "python2": '',

    "python3": python3.split()[1],
}
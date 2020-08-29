import subprocess


def extract(dataset):
    execute = ["java", "-jar", "../jars/irbench-v0.0.1-beta.2.jar", "-questions", dataset]
    return subprocess.run(execute, capture_output=True).stdout.decode()


for i in range(3, 10):
    with open('qald-'+str(i)+'-train.json', 'w') as f:
        data = extract("qald-"+str(i)+"-train-multilingual")
        f.write(data)

    with open('qald-'+str(i)+'-test.json', 'w') as f:
        data = extract("qald-"+str(i)+"-test-multilingual")
        f.write(data)

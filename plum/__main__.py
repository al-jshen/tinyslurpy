import subprocess


def main():
    jobname = input("Job name: ")
    nodes = input("Nodes (default 1): ") or 1
    tasks = input("Tasks (default 1): ") or 1
    cpus_per_task = input("CPUs per task (default 1): ") or 1
    gpus = input("GPUs (default 1): ") or 1
    mem_per_cpu = input("Memory per CPU (default 10G): ") or "10G"
    time = input("Time (default 00:10:00): ") or "00:10:00"
    email = input("Email (default js5013@princeton.edu): ") or "js5013@princeton.edu"
    command = input("Command: ")

    batch_file = f"""#!/bin/bash
    Hello! My name is Slurpy :) \nI'd love to help you with your slurm job. Can you please give me the following info and I'll write your file for you! <3
#SBATCH --job-name={jobname}
#SBATCH --output={jobname}.out
#SBATCH --error={jobname}.err
#SBATCH --nodes={nodes}
#SBATCH --ntasks={tasks}
#SBATCH --cpus-per-task={cpus_per_task}
"""
    if int(gpus) > 0:
        batch_file += f"""\n#SBATCH --gres=gpu:{gpus}"""

    batch_file += f"""\n#SBATCH --mem-per-cpu={mem_per_cpu}
#SBATCH --time={time}
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --mail-user={email}

{command}
    """

    run = input("Run? (Y/n): ") or "y"

    if run.lower() == "n":
        print(batch_file)
    elif run.lower() == "y":
        with open(f"{jobname}.slurm", "w") as f:
            f.write(batch_file)
        subprocess.run(["sbatch", f"{jobname}.slurm"])
        subprocess.run(["rm", f"{jobname}.slurm"])


if __name__ == "__main__":
    main()

import subprocess


def main():
    print(
        "Hello! My name is Slurpy :) I'd love to help you with your Slurm job. Can you please give me the following info and I'll write your file for you! <3"
    )

    jobname = input('Job name (default "slurpy"): ') or "slurpy"
    nodes = input("Nodes (default 1): ") or 1
    tasks_per_node = input("Tasks per node (default 1): ") or 1
    cpus_per_task = input("CPUs per task (default 1): ") or 1
    gpus_per_task = input("GPUs per task (default 0): ") or 0
    constraint = input("Constraint (default none): ") or None
    partition = input("Partition (default none): ") or None
    mem = input("Total memory (default 50G): ") or "50G"
    time = input("Time (default 00:10:00): ") or "00:10:00"
    email = input("Email (default none): ") or None
    command = input("Command: ")
    save = input("Save file? (Y/n): ") or "y"
    run = input("Run? (Y/n): ") or "y"

    batch_file = f"""#!/bin/bash
#SBATCH --job-name={jobname}
#SBATCH --output={jobname}.out
#SBATCH --error={jobname}.err
#SBATCH --nodes={nodes}
#SBATCH --ntasks-per-node={tasks_per_node}
#SBATCH --cpus-per-task={cpus_per_task}
"""

    if int(gpus_per_task) > 0:
        batch_file += f"""\n#SBATCH --gpus-per-task={gpus_per_task}"""
    if constraint is not None:
        batch_file += f"""\n#SBATCH --constraint={constraint}"""
    if partition is not None:
        batch_file += f"""\n#SBATCH --partition={partition}"""

    batch_file += f"""\n#SBATCH --mem={mem}
#SBATCH --time={time}"""

    if email is not None:
        batch_file += f"""\n#SBATCH --mail-type=ALL
#SBATCH --mail-user={email}"""

    batch_file += f"""\n\n{command}"""

    with open(f"{jobname}.slurm", "w") as f:
        f.write(batch_file)

    if run.lower() in ["n", "no"]:
        print(batch_file)
    elif run.lower() in ["y", "yes"]:
        subprocess.run(["sbatch", f"{jobname}.slurm"])

    if save.lower() in ["n", "no"]:
        subprocess.run(["rm", f"{jobname}.slurm"])

    print(
        "Thanks for letting me help you write your slurm file, I'm always here to help! ^_^ Bye for now <3"
    )


if __name__ == "__main__":
    main()

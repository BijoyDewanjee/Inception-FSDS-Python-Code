
# For installed Packet list
pip list

# Create Virtual environment
conda create -n project name/ enviroment name package name -y
For Example:
            conda create -n helmet python=3.9 -y
# For Activate Environment:

            conda activate helmet
# To Watch Environment list

            conda env list
# To Delete environment folder or project folder

            conda remove --name helmet --all

# Vs Code a korte gale
conda create --prefix .\helmet python=3.9 -y

conda activate .\helmet

# Requirement a onnek gulo package ak sathe install korar jonno:
pip install -r requirement.txt


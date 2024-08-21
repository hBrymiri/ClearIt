from setuptools import setup, find_packages

setup(
    
 name = 'clearIt',  # name of project"
 version='0.1',  # this is the current pack of all pckages"
 packages=find_packages(), #this line finds all packages"
 install_requires=[],
 entry_point={
     'console_scripts': [
         'clearit = clearIt.main:main_function',
     ]
 },
 
 author= 'Bryan H , Drake H',
 author_email='BryanH1221@gmail.com',
 description=' An extentsion that deletes unwated mail',
 long_description=open("README.md").read(),
 long_description_content_type='text/markdown',
 url='https://github.com/hBrymiri/ClearIt.git', # url to project
 classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',  
 ],
 
        
)
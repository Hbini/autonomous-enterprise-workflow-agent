from setuptools import setup, find_packages
setup(name='autonomous-enterprise-workflow-agent', version='0.1.0', author='Hernane Bini', description='Autonomous Enterprise Workflow Agent', packages=find_packages(), python_requires='>=3.9', install_requires=['airflow>=2.7.0', 'celery>=5.3.0', 'fastapi>=0.104.0', 'pytest>=7.4.0'])

from setuptools import setup, find_packages

setup(
    name="research_prep_agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Will be read from requirements.txt
    ],
    author="Sam Star",
    author_email="samstar2809@gmail.com",
    description="A Research and Preparation agent for job searching and application materials",
    keywords="job search, resume, cover letter, automation",
    python_requires=">=3.8",
)
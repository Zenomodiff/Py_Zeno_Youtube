import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Zeno_Youtube",
    version="1",
    author="Sreeram Aj",
    author_email="sreeramzeno@gmail.com",
    description="This Package Was Made For Those Who Love Youtube. It Gives Random Youtube Video Links, Youtube Video Titles and Also As A Mix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zenomodiff/Py_Zeno_Youtube",
    project_urls={
        "Bug Tracker": "https://github.com/Zenomodiff/Py_Zeno_Youtube/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9.6",
)

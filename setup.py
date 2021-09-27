import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtube-search-python",
    version="1.4.9",
    author="Hitesh Kumar Saini",
    license='MIT',
    author_email="saini123hitesh@gmail.com",
    description="Search for YouTube videos, channels & playlists & get video information using link WITHOUT YouTube Data API v3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexmercerind/youtube-search-python",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'httpx'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

from distutils.core import setup

setup(
    name = "slingshot",
    packages = "slingshot",
    version = "0.5",
    license = "MIT",
    description = "Slingshot is a Python library bringed on by A Mosca team for creating reproducible procedural documents for Brazilian law-suits.",
    author = "A Mosca",
    author_email = "staff.amosca@gmail.com",
    download_url = "https://github.com/amosca-team/slingshot/archive/0.5.2.tar.gz",
    install_requires = ["pdfkit",
                        "pandoc",
                        "markdown"
                        ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers, Law students",
        "Programming Language :: Python 3.7"
    ]
)
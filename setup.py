from setuptools import setup, find_packages

setup(
    name="code-snippet-manager",  # your package name
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "snipman=snippet_manager.cli:system",  # command to run CLI
        ],
    },
    include_package_data=True,
    description="A terminal-based code snippet manager",
    python_requires=">=3.10",
)

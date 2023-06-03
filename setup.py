from setuptools import setup

setup(
      name="statsHypo",
      version="1.0",
      description="Library of statistical hypothesis tests",
      author="Ziad Ghauch",
      url="https://github.com/ZGGhauch/statsHypo",
      packages=["statsHypo"],
      include_package_data=True,
      requires=["numpy","scipy"]
)

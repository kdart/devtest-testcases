Base Test Cases
===============

A python package namespace that establishes the *testcases* namespace package.
Other packages can use this namespace to install test cases.

Will also provide special test case support, such as documentation generators.

The devtest framework uses this as the base package name to find test cases
to run.

Other package distributions may use the "testcases" base package to install
additional test cases for any project.

This project may also be used as a template for other testcases packages. Since
it uses the setuptools namespace feature, all such packages will have the root
package name of "testcases". The framework, by default, search for test case
implementations in this namespace.

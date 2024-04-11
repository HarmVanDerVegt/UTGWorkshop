# UTG workshop
We have had a quick look into what a UTG is, what types there are and how to evaluate them.

Now we can get some hands on experience with using and evaluating UTGs.

Dependig on which group you are in you will use and evaluate either CodiumAI or Pynguin.

Evaluating CodiumAI can be done on your own computer if you have VSCode installed.

Evaluating Pynguin must be done in groups, with a laptop that has Pynguin installed and set up. The workshop will provide these laptops.

The UTGs will be run on this the code provided in this repository.

## Workshop agenda
The aim of the workshop is to gain a look into the pratical usage of UTGs and how to evaluate their output.

We do this by running the UTG on the code provided, running the generated tests and noting which passed or failed. and gathering coverage data.

We then generate the coverage report, giving us one of the quality metrics.

Then we make some mutations to our code base, change a 0 to a 1 or change an operator and the like. Make note of how many (and which) mutations you introduce.

Run the tests again, note again which passed or failed. We have now done manual mutation testing.

Write your team name down on the whiteboard together with the following data:

1. Tested UTG
2. Coverage percentage
3. Percentage of mutants killed

We have 50 minutes.

5 minutes, explaining the workshop and creating groups

10 minutes, setup of CodiumAI and Pynguin, downloading of the repository

20 minutes, creating tests and evaluating chosen UTG

5 minutes, discussion in your group on the effectiveness of you UTG

10 minutes, presentation of thoughts of each group



## Essential commands

Running the tests
`coverage run -m pytest <test or .>`

Creating the report
`coverage html`
Find the report at `htmlcov/index.html`

Removing previously gathered coverage data
`coverage erase`

## Pynguin commands

There is one pynguin command that we use today, the command to create tests.

Run this command in the `pynguin` subdirectory.

1. `cd pynguin`
2. 
`pynguin --project_path=.. --module_name=<module name> --output_path=. --assertion_generation=MUTATION_ANALYSIS --allow_stale_assertions --algorithm WHOLE_SUITE`

Substitute `<module name>` for the name of the module you wish to create tests for, `fibonacci` for example if you want to create tests for `fibonacci.py`.

Pynguin might generate some tests that are decorated with an xfail decorator. This means that the program returned an unexpected exception while using these inputs, this too can be considered a regression test (or could serve as a reminder to crash more gracefully).

## CodiumAI usage
NOTE: To reliably use CodiumAI you will need to be on a different network than XS4OFFICE. Turn on your hotspot or join someone elses.

Open VSCode and install the `Codiumate` extension.

Log in with the credentials given to you by the instructors.

If you've installed the extension correctly, there should be both a CodiumAI icon on the left and a CodiumAI prompt button above classes and functions. If not, please turn to an instructor.

To generate tests for a class or for an individual function, press the `Generate tests` button above the corresponding class or function.

Save the generated tests in a file in the `codiumai` folder.

## Notes on source files
Can't include meta comments in the source file or CodiumAI will pick them up.

`flight.py` includes several unused paramaters in its functions, how does each UTG deal with that?

`factorial.py` can take ages to complete if given a large enough number, this should not be an issue for CodiumAI, but Pynguin might have an issue with this.

## EXTRA (only if you have time left over)
All of the code examples are without type hints, how does adding type hints impact the generation of tests?

1. Add type hints
2. Generate tests again
3. GOather data
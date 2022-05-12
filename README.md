# DCPAutomate
This is an effort to automate my workflow to solve daily coding problem sets from https://www.dailycodingproblem.com/

# Version History

## 0.1
- Skeleton for documentation on README
- Defined Desired Outcome
- Defined Project Requirements
- Defined Proposed Procedure.
- Updated commit message in Current Progress (###)

# Desired Outcome
Everyday, I work on 1-3 problems on a Daily Coding Problem set. I work on the single problem
that was released today. With 100s of problems having been released before I joined, I add to my practice
by working on some past problems as well, randomly selected out of problems I haven't visited before. 

Everytime I attempt a problem, I take some time to do the following:
1. Explore and understand the problem.
2. Design and develop an algorithm.
3. Write some code to implement the algorithm.
4. Write some code to test the algorithm.
5. Write some code to adhere to edge cases.
6. Read over the solution (if available) and implement that as well.

This process is well structured and follows an orderly routine. Therefore, to cut out some workflow-related
machinery, I want to automate some of the above steps by adding some skeleton code and space to outline my thoughts.

# Project Requirements
A successfully written program will:
1. Prompt me to get how many problems I want to solve today.
2. Access today's DCP along with any additional ones based on number of problems.
3. Parse the DCP email to extract the problem.
4. Create a text file for algorithm design.
5. Prompt me to get which languages I want to use to write an implementation and generate development files based on that response.
6. Generate some comments onto those development files.
7. Add test functions to the development files.
8. Develop a README to display success and results.

# Proposed Procedure
In order to complete this project, here is the suggested flow:
1. Figure out how to access my Gmail inbox for DCP emails.
2. Parse a DCP email for key information.
3. Determine file creation and naming scheme.
4. Determine file content structure (testing code, driver code, comments, etc.)
5. Add essential I/O
6. Determine output scheme for README file (potential wrapper code for executing git commands?)

# Current Progress
1. The I/O flow has been built in `script.sh`
2. Figured out how to interface with the Gmail API and have tokens and other essential information saved.
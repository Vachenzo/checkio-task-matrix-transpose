"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            "answer": [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9]
            ]
        },
        {
            "input": [
                [1, 4, 3],
                [8, 2, 6],
                [7, 8, 3],
                [4, 9, 6],
                [7, 8, 1]
            ],
            "answer": [
                [1, 8, 7, 4, 7],
                [4, 2, 8, 9, 8],
                [3, 6, 3, 6, 1]
            ]
        },
        {
            "input": [
                [7, 1, 1, 2, 2],
                [0, 2, 6, 1, 5],
                [2, 4, 2, 4, 2],
                [4, 0, 6, 6, 7],
                [0, 6, 0, 1, 5]
            ],
            "answer": [
                [7, 0, 2, 4, 0],
                [1, 2, 4, 0, 6],
                [1, 6, 2, 6, 0],
                [2, 1, 4, 6, 1],
                [2, 5, 2, 7, 5]
            ]
        },
        {
            "input": [
                [7],
                [4],
                [9],
                [7]
            ],
            "answer": [
                [7, 4, 9, 7]
            ]
        },
        {
            "input": [
                [5, 5, 0, 7],
                [5, 4, 8, 3],
                [8, 7, 0, 7]
            ],
            "answer": [
                [5, 5, 8],
                [5, 4, 7],
                [0, 8, 0],
                [7, 3, 7]
            ]
        },
        {
            "input": [
                [9, 3, 2],
                [8, 7, 9]
            ],
            "answer": [
                [9, 8],
                [3, 7],
                [2, 9]
            ]
        },
        {
            "input": [
                [7, 6],
                [6, 9],
                [7, 8],
                [6, 6],
                [4, 5],
                [6, 2]
            ],
            "answer": [
                [7, 6, 7, 6, 4, 6],
                [6, 9, 8, 6, 5, 2]
            ]
        },
        {
            "input": [
                [1, 8]
            ],
            "answer": [
                [1],
                [8]
            ]
        },
        {
            "input": [
                [6, 9, 0, 2, 3],
                [2, 7, 5, 4, 6]
            ],
            "answer": [
                [6, 2],
                [9, 7],
                [0, 5],
                [2, 4],
                [3, 6]
            ]
        },
        {
            "input": [
                [8],
                [7],
                [5],
                [7],
                [5],
                [2]
            ],
            "answer": [
                [8, 7, 5, 7, 5, 2]
            ]
        },
        {
            "input": [
                [7, 4, 2, 1, 1, 6],
                [8, 3, 2, 7, 8, 6],
                [8, 8, 3, 5, 1, 5]
            ],
            "answer": [
                [7, 8, 8],
                [4, 3, 8],
                [2, 2, 3],
                [1, 7, 5],
                [1, 8, 1],
                [6, 6, 5]
            ]
        },
        {
            "input": [
                [6, 3, 5, 4]
            ],
            "answer": [
                [6],
                [3],
                [5],
                [4]
            ]
        },
        {
            "input": [
                [5, 0, 3],
                [4, 6, 3],
                [4, 7, 2]
            ],
            "answer": [
                [5, 4, 4],
                [0, 6, 7],
                [3, 3, 2]
            ]
        },
        {
            "input": [
                [1],
                [3],
                [5],
                [6],
                [3]
            ],
            "answer": [
                [1, 3, 5, 6, 3]
            ]
        },
        {
            "input": [
                [4, 3],
                [2, 2],
                [7, 8]
            ],
            "answer": [
                [4, 2, 7],
                [3, 2, 8]
            ]
        },
        {
            "input": [
                [0, 6, 4, 0],
                [6, 5, 6, 0]
            ],
            "answer": [
                [0, 6],
                [6, 5],
                [4, 6],
                [0, 0]
            ]
        },
        {
            "input": [
                [1, 6, 8, 9, 8],
                [5, 5, 1, 5, 8],
                [1, 0, 6, 1, 9],
                [5, 1, 5, 9, 3],
                [6, 1, 6, 7, 3],
                [3, 6, 8, 1, 6]
            ],
            "answer": [
                [1, 5, 1, 5, 6, 3],
                [6, 5, 0, 1, 1, 6],
                [8, 1, 6, 5, 6, 8],
                [9, 5, 1, 9, 7, 1],
                [8, 8, 9, 3, 3, 6]
            ]
        },
        {
            "input": [
                [7, 5, 6],
                [1, 8, 9],
                [5, 1, 6],
                [5, 0, 8],
                [1, 6, 3],
                [6, 9, 8]
            ],
            "answer": [
                [7, 1, 5, 5, 1, 6],
                [5, 8, 1, 0, 6, 9],
                [6, 9, 6, 8, 3, 8]
            ]
        },
        {
            "input": [
                [1]
            ],
            "answer": [
                [1]
            ]
        }
    ],
    "Extra": [
        {
            "input": [
                [9, 7],
                [7, 2],
                [6, 4]
            ],
            "answer": [
                [9, 7, 6],
                [7, 2, 4]
            ]
        },
        {
            "input": [
                [1, 6],
                [4, 5],
                [2, 7]
            ],
            "answer": [
                [1, 4, 2],
                [6, 5, 7]
            ]
        },
        {
            "input": [
                [6, 2, 9, 1, 8, 8],
                [6, 0, 8, 5, 5, 8],
                [4, 1, 2, 4, 9, 7],
                [7, 1, 4, 2, 0, 7],
                [0, 6, 4, 6, 5, 4]
            ],
            "answer": [
                [6, 6, 4, 7, 0],
                [2, 0, 1, 1, 6],
                [9, 8, 2, 4, 4],
                [1, 5, 4, 2, 6],
                [8, 5, 9, 0, 5],
                [8, 8, 7, 7, 4]
            ]
        },
        {
            "input": [
                [7, 8, 4, 9],
                [0, 8, 2, 9],
                [3, 8, 7, 7],
                [6, 2, 0, 4],
                [4, 9, 4, 1]
            ],
            "answer": [
                [7, 0, 3, 6, 4],
                [8, 8, 8, 2, 9],
                [4, 2, 7, 0, 4],
                [9, 9, 7, 4, 1]
            ]
        },
        {
            "input": [
                [6],
                [3],
                [0],
                [3],
                [1],
                [2]
            ],
            "answer": [
                [6, 3, 0, 3, 1, 2]
            ]
        },
        {
            "input": [
                [2, 5, 1, 4, 4],
                [5, 5, 2, 9, 8],
                [7, 4, 2, 2, 1]
            ],
            "answer": [
                [2, 5, 7],
                [5, 5, 4],
                [1, 2, 2],
                [4, 9, 2],
                [4, 8, 1]
            ]
        },
        {
            "input": [
                [6, 1, 5],
                [5, 9, 9],
                [5, 5, 1],
                [0, 7, 5],
                [5, 1, 2]
            ],
            "answer": [
                [6, 5, 5, 0, 5],
                [1, 9, 5, 7, 1],
                [5, 9, 1, 5, 2]
            ]
        },
        {
            "input": [
                [7],
                [7],
                [3],
                [4]
            ],
            "answer": [
                [7, 7, 3, 4]
            ]
        },
        {
            "input": [
                [7, 4, 5, 6, 9, 9]
            ],
            "answer": [
                [7],
                [4],
                [5],
                [6],
                [9],
                [9]
            ]
        },
        {
            "input": [
                [1, 5, 0, 4, 2],
                [5, 2, 7, 4, 7],
                [0, 9, 6, 7, 4],
                [4, 9, 1, 9, 8],
                [5, 3, 6, 7, 1],
                [9, 6, 1, 6, 8]
            ],
            "answer": [
                [1, 5, 0, 4, 5, 9],
                [5, 2, 9, 9, 3, 6],
                [0, 7, 6, 1, 6, 1],
                [4, 4, 7, 9, 7, 6],
                [2, 7, 4, 8, 1, 8]
            ]
        },
        {
            "input": [
                [0, 2, 4, 2, 2],
                [5, 1, 8, 9, 2],
                [3, 6, 7, 7, 7],
                [7, 7, 6, 0, 0]
            ],
            "answer": [
                [0, 5, 3, 7],
                [2, 1, 6, 7],
                [4, 8, 7, 6],
                [2, 9, 7, 0],
                [2, 2, 7, 0]
            ]
        },
        {
            "input": [
                [2, 0, 3, 5, 2, 3],
                [4, 6, 1, 7, 8, 9],
                [6, 4, 1, 8, 8, 6],
                [1, 0, 6, 7, 2, 2],
                [7, 0, 0, 0, 8, 1],
                [9, 5, 2, 0, 2, 7]
            ],
            "answer": [
                [2, 4, 6, 1, 7, 9],
                [0, 6, 4, 0, 0, 5],
                [3, 1, 1, 6, 0, 2],
                [5, 7, 8, 7, 0, 0],
                [2, 8, 8, 2, 8, 2],
                [3, 9, 6, 2, 1, 7]
            ]
        },
        {
            "input": [
                [6]
            ],
            "answer": [
                [6]
            ]
        },
        {
            "input": [
                [0, 5, 7],
                [6, 6, 2],
                [5, 1, 6],
                [2, 8, 1],
                [2, 5, 7]
            ],
            "answer": [
                [0, 6, 5, 2, 2],
                [5, 6, 1, 8, 5],
                [7, 2, 6, 1, 7]
            ]
        },
        {
            "input": [
                [8],
                [4],
                [0],
                [6]
            ],
            "answer": [
                [8, 4, 0, 6]
            ]
        },
        {
            "input": [
                [6, 8, 9],
                [1, 2, 0],
                [2, 0, 0],
                [2, 3, 5]
            ],
            "answer": [
                [6, 1, 2, 2],
                [8, 2, 0, 3],
                [9, 0, 0, 5]
            ]
        },
        {
            "input": [
                [5],
                [1],
                [8],
                [4]
            ],
            "answer": [
                [5, 1, 8, 4]
            ]
        },
        {
            "input": [
                [8, 0, 0],
                [3, 2, 7]
            ],
            "answer": [
                [8, 3],
                [0, 2],
                [0, 7]
            ]
        },
        {
            "input": [
                [7, 8, 5],
                [7, 0, 4],
                [7, 5, 2],
                [9, 5, 3],
                [8, 0, 3]
            ],
            "answer": [
                [7, 7, 7, 9, 8],
                [8, 0, 5, 5, 0],
                [5, 4, 2, 3, 3]
            ]
        },
        {
            "input": [
                [0, 8, 3, 6],
                [5, 1, 1, 5]
            ],
            "answer": [
                [0, 5],
                [8, 1],
                [3, 1],
                [6, 5]
            ]
        },
        {
            "input": [
                [5, 3, 8],
                [0, 2, 5],
                [4, 6, 9],
                [5, 5, 4],
                [2, 4, 3],
                [8, 9, 0]
            ],
            "answer": [
                [5, 0, 4, 5, 2, 8],
                [3, 2, 6, 5, 4, 9],
                [8, 5, 9, 4, 3, 0]
            ]
        },
        {
            "input": [
                [6, 0, 1]
            ],
            "answer": [
                [6],
                [0],
                [1]
            ]
        },
        {
            "input": [
                [2, 4, 1, 9, 9]
            ],
            "answer": [
                [2],
                [4],
                [1],
                [9],
                [9]
            ]
        },
        {
            "input": [
                [1]
            ],
            "answer": [
                [1]
            ]
        },
        {
            "input": [
                [3, 1, 2, 5, 2],
                [8, 8, 2, 7, 4]
            ],
            "answer": [
                [3, 8],
                [1, 8],
                [2, 2],
                [5, 7],
                [2, 4]
            ]
        },
        {
            "input": [
                [6, 3, 7],
                [7, 2, 8],
                [0, 5, 0]
            ],
            "answer": [
                [6, 7, 0],
                [3, 2, 5],
                [7, 8, 0]
            ]
        },
        {
            "input": [
                [1, 1, 4, 4, 6, 1],
                [6, 4, 6, 6, 2, 0]
            ],
            "answer": [
                [1, 6],
                [1, 4],
                [4, 6],
                [4, 6],
                [6, 2],
                [1, 0]
            ]
        },
        {
            "input": [
                [9, 0],
                [5, 9],
                [5, 6],
                [4, 3],
                [0, 2]
            ],
            "answer": [
                [9, 5, 5, 4, 0],
                [0, 9, 6, 3, 2]
            ]
        },
        {
            "input": [
                [9, 7, 1, 6, 6, 4],
                [7, 8, 5, 4, 0, 4],
                [9, 0, 4, 5, 1, 7],
                [7, 0, 2, 6, 6, 0],
                [5, 1, 7, 4, 1, 1]
            ],
            "answer": [
                [9, 7, 9, 7, 5],
                [7, 8, 0, 0, 1],
                [1, 5, 4, 2, 7],
                [6, 4, 5, 6, 4],
                [6, 0, 1, 6, 1],
                [4, 4, 7, 0, 1]
            ]
        }
    ]
}

/* Solves one of those triangle shaped peg jumping puzzles.
   You begin with a board composed of n rows, where the i-th
   row contains i columns. e.g.:
       X
      X X
     X X X
   The board begins with pegs in all holes but one. A peg can
   jump over another peg if it can land in a hole on the other
   side. The jumped peg is removed. The goal is to finish with
   a single peg remaining.
*/

#include<stdio.h>
#include<stdlib.h>
#define PUZZROWS 5
#define PEGS (PUZZROWS * (PUZZROWS + 1)) / 2

typedef struct board {
  int peg[PEGS]; // each board will represent its pegs by arrays of integers
  int *row[PUZZROWS]; // these rows will point at the pegs
  int lastMove;
  struct board *previousPosition; //the board layout prior to this one
} Board;

typedef struct searchqueuenode { // Search will be depth-first with a linked list
  Board *board;
  struct searchqueuenode *next;
} Node;

void intArrayToBoard(int startboardAsIntArray[], Board *firstmove);
void printBoard(Board *layout);
void printList(Node *node);
int winningPosition(Board *b);
void removeFirstAndEnqueuePossibleMoves(Node **queue);
void runSomeTests();
Board *boardFromJumpUpAndLeft(Board*, int, int);
Board *reverseBoardOrder(Board*);
void printBoardList(Board*);

Node *queue; //List of to-be-examined nodes, "queue" points to the first one
int totalpossibilities=0;

main() {
  int startboard[] = {
        0,
       1, 1,
      1, 1, 1,
     1, 1, 1, 1,
    1, 1, 1, 1, 1,
  };
  int i;
  Board first, *solution;

  //testing
  Board *testBoard;
  Node *testNode;



  //;;;;;;;;;; Testing portion ;;;;;;;;;;

  /* printf("Testing intArrayToBoard and printBoard:\n"); */
  /* // Initialize starting position, and linked list */
  /* intArrayToBoard(startboard, &first); */
  /* first.previousPosition = NULL; */
  /* printBoard(&first); */

  /* printf("Testing boardFromJumpUpAndLeft:\n"); */
  /* testBoard = boardFromJumpUpAndLeft(&first, 2, 2); */
  /* printBoard(testBoard); */

  /* printf("Testing Queue. Expect same board as first\n"); */
  /* queue = (Node *) malloc(sizeof(Node)); */
  /* queue->board = &first; */
  /* queue->next = NULL; */
  /* printBoard(queue->board); */

  /* printf("Testing printList:\n"); */
  /* testNode = malloc(sizeof(Node)); */
  /* testNode->board = testBoard; */
  /* testNode->next = queue; */
  /* printList(testNode); */

  /* printf("Testing removeFirstAndEnqueuePossibleMoves:\n"); */
  /* removeFirstAndEnqueuePossibleMoves(&queue); */
  /* printList(queue); */

  //;;;;;;;;;; End testing ;;;;;;;;;;


  intArrayToBoard(startboard, &first);
  first.previousPosition = NULL;
  queue = (Node *) malloc(sizeof(Node));
  queue->board = &first;
  queue->next = NULL;

  while( queue != NULL ) {
    if (winningPosition(queue->board))
      break;
    removeFirstAndEnqueuePossibleMoves(&queue);
  }

  if (!queue) {
    printf("No solution found.\n");
  } else {
    printf("Starting board:\n");
    printBoard(&first);
    printf("Boards generated: %d\n", totalpossibilities);
    printf("Solution:\n");
    solution = reverseBoardOrder(queue->board);
    printBoardList(solution);
  }

  return 0;
}

void removeFirstAndEnqueuePossibleMoves(Node **q) {
  int r, c;
  Board *parentBoard, *newBoard;
  Node *newNodeList = NULL, *tempListPtr;

  Board *boardFromJumpUpAndLeft(Board*, int row, int col);
  Board *boardFromJumpUpAndRight(Board*, int row, int col);
  Board *boardFromJumpLeft(Board*, int row, int col);
  Board *boardFromJumpRight(Board*, int row, int col);
  Board *boardFromJumpDownAndLeft(Board*, int row, int col);
  Board *boardFromJumpDownAndRight(Board*, int row, int col);

  void addBoardToFrontOfList(Board*, Node **);

  parentBoard = (*q)->board;

  // Generate new possible boards, and add to newNodeList
  for(r=0; r<PUZZROWS; r++) {
    for(c=0; c<r+1; c++) {
      if (*(parentBoard->row[r]+c) == 1) { //This space has a peg
	if (newBoard = boardFromJumpUpAndLeft(parentBoard, r, c)) {
	  addBoardToFrontOfList(newBoard, &newNodeList);
	  totalpossibilities++;
	}
	if (newBoard = boardFromJumpUpAndRight(parentBoard, r, c)) {
	  addBoardToFrontOfList(newBoard, &newNodeList);
	  totalpossibilities++;
	}
	if (newBoard = boardFromJumpLeft(parentBoard, r, c)) {
	  addBoardToFrontOfList(newBoard, &newNodeList);
	  totalpossibilities++;
	}
	if (newBoard = boardFromJumpRight(parentBoard, r, c)) {
	  addBoardToFrontOfList(newBoard, &newNodeList);
	  totalpossibilities++;
	}
	if (newBoard = boardFromJumpDownAndLeft(parentBoard, r, c)) {
	  addBoardToFrontOfList(newBoard, &newNodeList);
	  totalpossibilities++;
	}
	if (newBoard = boardFromJumpDownAndRight(parentBoard, r, c)) {
	  addBoardToFrontOfList(newBoard, &newNodeList);
	  totalpossibilities++;
	}
      }
    }
  }

  // Drop queue's first element, add newNodeList (if not null) to front
  // Warning! Memory Leak! But can't free a board's parents -- figure out later
  // maybe keep a visited list or something. Shouldn't be *too* many possible
  // boards so I don't think the leak will be that big.
  if (newNodeList) {
    tempListPtr = (*q)->next;
    *q = newNodeList;
    while (newNodeList->next) // Get to end of list
      newNodeList = newNodeList->next;
    newNodeList->next = tempListPtr;
  } else {
    *q = (*q)->next;
  }
}

Board *boardFromJumpUpAndLeft(Board *parent, int row, int col) {
  Board *newBoard = NULL;
  Board *copyBoard(Board *);

  if  ( row-2 >= 0 // two rows up is part of puzzle
	&& col-2 >=0 // two columns left is part of puzzle
	&& *(parent->row[row-2] + (col-2)) == 0 // landing space is empty
	&& *(parent->row[row-1] + (col-1)) == 1 // there is a peg to jump
	) {
    newBoard = copyBoard(parent);
    newBoard->previousPosition = parent;
    newBoard->lastMove=0;
    *(newBoard->row[row-1] + (col-1)) = 0;
    *(newBoard->row[row-2] + (col-2)) = 1;
    *(newBoard->row[row] + col) = 0;

    return newBoard;
  } else {
    return NULL; // Not a valid move
  }
}

Board *boardFromJumpUpAndRight(Board *parent, int row, int col) {
  Board *newBoard = NULL;
  Board *copyBoard(Board *);

  if  ( row-2 >= 0 // two rows up is part of puzzle
	&& col <= row-2 // column is left enough that jumping up won't leave puzzle
	&& *(parent->row[row-2] + col) == 0 // landing space is empty
	&& *(parent->row[row-1] + col) == 1 // there is a peg to jump
	) {
    newBoard = copyBoard(parent);
    newBoard->previousPosition = parent;
    newBoard->lastMove=1;
    *(newBoard->row[row-1] + col) = 0;
    *(newBoard->row[row-2] + col) = 1;
    *(newBoard->row[row] + col) = 0;

    return newBoard;
  } else {
    return NULL; // Not a valid move
  }
}

Board *boardFromJumpLeft(Board *parent, int row, int col) {
  Board *newBoard = NULL;
  Board *copyBoard(Board *);

  if  ( col-2 >= 0 // two columns left is part of puzzle
	&& *(parent->row[row] + (col-2)) == 0 // landing space is empty
	&& *(parent->row[row] + (col-1)) == 1 // there is a peg to jump
	) {
    newBoard = copyBoard(parent);
    newBoard->previousPosition = parent;
    newBoard->lastMove=2;
    *(newBoard->row[row] + (col-1)) = 0;
    *(newBoard->row[row] + (col-2)) = 1;
    *(newBoard->row[row] + col) = 0;

    return newBoard;

  } else {
    return NULL; // Not a valid move
  }
}

Board *boardFromJumpRight(Board *parent, int row, int col) {
  Board *newBoard = NULL;
  Board *copyBoard(Board *);

  if  ( col+2 <= row // two columns right is part of puzzle (# col's in row == row #)
	&& *(parent->row[row] + (col+2)) == 0 // landing space is empty
	&& *(parent->row[row] + (col+1)) == 1 // there is a peg to jump
	) {
    newBoard = copyBoard(parent);
    newBoard->previousPosition = parent;
    newBoard->lastMove=3;
    *(newBoard->row[row] + (col+1)) = 0;
    *(newBoard->row[row] + (col+2)) = 1;
    *(newBoard->row[row] + col) = 0;

    return newBoard;

  } else {
    return NULL; // Not a valid move
  }
}

// Note: Because array layout is right triangle, "down and left"
// is really straight down (maintains same column.
Board *boardFromJumpDownAndLeft(Board *parent, int row, int col) {
  Board *newBoard = NULL;
  Board *copyBoard(Board *);

  if  ( row+2 < PUZZROWS // down two rows is part of puzzle
	&& *(parent->row[row+2] + col) == 0 // landing space is empty
	&& *(parent->row[row+1] + col) == 1 // there is a peg to jump
	) {
    newBoard = copyBoard(parent);
    newBoard->previousPosition = parent;
    newBoard->lastMove=4;
    *(newBoard->row[row+1] + col) = 0;
    *(newBoard->row[row+2] + col) = 1;
    *(newBoard->row[row] + col) = 0;

    return newBoard;
  } else {
    return NULL; // Not a valid move
  }
}

Board *boardFromJumpDownAndRight(Board *parent, int row, int col) {
  Board *newBoard = NULL;
  Board *copyBoard(Board *);

  if  ( row+2 < PUZZROWS // two rows down is part of puzzle
	// No need to check columns: puzzle is right triangle, expands right w/ jump
	&& *(parent->row[row+2] + (col+2)) == 0 // landing space is empty
	&& *(parent->row[row+1] + (col+1)) == 1 // there is a peg to jump
	) {
    newBoard = copyBoard(parent);
    newBoard->previousPosition = parent;
    newBoard->lastMove=5;
    *(newBoard->row[row+1] + (col+1)) = 0;
    *(newBoard->row[row+2] + (col+2)) = 1;
    *(newBoard->row[row] + col) = 0;

    return newBoard;
  } else {
    return NULL; // Not a valid move
  }
}



//// List of conditions is tricky -- I think "cleverness" is bad here.
//// e.g. when jumping "up and right" the column value stays the same
//// because although the real life equilateral board would jump to the right
//// the arrays I'm using here are a right triangle, and the jump is
//// straight up. But a jump straight to the right (with no up), really *is* to the
//// right in real life and in my arrays. So, decided not to use this function.
// Takes a board position and specified peg, and checks whether
// that peg can legally make any of the 6 possible jumps. A peg
// can jump diagonally up/down + left/right, as well as straight
// left and right. Returns a list of nodes with each of the
// Possible board positions.
/* Node *boardsFromPossibleJumps(Board *parent, int row, int col) { */
/*   Board *newBoard = NULL; */
/*   Node *possibleMoves = NULL; */
/*   int r, c;  */
/*   Board *copyBoard(Board *); */

/*   for(r = -1; r <= 1; r ++) { // row modifier: jump up, flat, or down? */
/*     for (c= -1; c <= 0; c++) { // column modifier: jump left or "right"? */
/*       if  ( row+(2*r) >= 0  */
/* 	    && row+(2*r) < PUZZROWS // landing row is part of puzzle */
/* 	    && col+(2*c) >=0 // landing col is part of puzzle */
/* 	    && col+(2*c) <= row+(2*r) // and # cols for a given row is equal to row # */
/* 	    && *(parent->row[row-2] + (col-2)) == 0 // landing space is empty */
/* 	    && *(parent->row[row-1] + (col-1)) == 1 // there is a peg to jump */
/* 	    ) { */
/* 	newBoard = copyBoard(parent); */
/* 	newBoard->previousPosition = parent; */
/* 	*(newBoard->row[row-1] + (col-1)) = 0; */
/* 	*(newBoard->row[row-2] + (col-2)) = 1; */
/* 	*(newBoard->row[row] + col) = 0; */

/* 	return newBoard; */
/*       } else { */
/* 	return NULL; // Not a valid move */
/*       } */
/*     } */
/*   } */
/* } */

Board *copyBoard(Board *oldBoard) {
  Board *newBoard;
  int i, triangleNumberOffset;

  if (newBoard = (Board*) malloc(sizeof(Board)) ){
    for(i=0; i<PEGS; i++) {
      newBoard->peg[i] = oldBoard->peg[i];
    }
    for(i=0, triangleNumberOffset=0; i<PUZZROWS; i++) {
      newBoard->row[i] = newBoard->peg + triangleNumberOffset;
      triangleNumberOffset += (i+1);
    }
    return newBoard;
  } else {
    return NULL;
  }
}

void addBoardToFrontOfList(Board *brd, Node **first) {
  Node *newNode;

  newNode = (Node*) malloc(sizeof(Node));
  newNode->board = brd;
  newNode->next = *first;
  *first = newNode;
}

int winningPosition(Board *b) {
  int i, pegcount=0;
  for (i=0; i<PEGS; i++) {
    if (b->peg[i] == 1)
      pegcount++;
  }
  return (pegcount == 1);
}

void intArrayToBoard(int boardAsIntArray[], Board *boardAsStruct) {
  int i, triangleNumberOffset;

  for(i=0; i<PEGS; i++) {
    boardAsStruct->peg[i] = boardAsIntArray[i];
  }
  for(i=0, triangleNumberOffset=0; i<PUZZROWS; i++) {
    boardAsStruct->row[i] = boardAsStruct->peg + triangleNumberOffset;
    triangleNumberOffset += (i+1);
  }
}

void printBoard(Board *boardLayout) {
  int i, j, k;
  for(i=0; i<PUZZROWS; i++){
    for(k=0; k<(PUZZROWS-1)-i; k++) { // white space to center rows
      printf(" ");
    }
    for(j=0; j<i+1; j++) {
      printf("%d ",*((boardLayout->row[i])+j));
    }
    printf("\n");
  }
  printf("By doing: %d\n\n",boardLayout->lastMove);
}

void printList(Node *node) {
  while (node) {
    printBoard(node->board);
    node = node->next;
  }
}

// Takes a Board* and reverses the chain of "previousPosition"s, returns the new first
Board *reverseBoardOrder(Board *first) {
  Board *child, *parent;

  for(child=NULL; first->previousPosition; first = parent) {
    parent = first->previousPosition;
    first->previousPosition = child;
    child = first;
  }
  first->previousPosition = child;
  return first;
}

void printBoardList(Board *first) {
  while (first) {
    printBoard(first);
    first = first->previousPosition;
  }
}

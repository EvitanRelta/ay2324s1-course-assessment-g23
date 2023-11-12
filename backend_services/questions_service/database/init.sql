DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_user WHERE usename = 'user') THEN
        CREATE USER "user" WITH PASSWORD 'password';
    END IF;
END $$;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS questions(
    question_id VARCHAR(255) PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(255) NOT NULL,
    complexity VARCHAR(255) NOT NULL
);
INSERT INTO questions (question_id, title, description, category, complexity)
VALUES
(uuid_generate_v4()::VARCHAR, 'Reverse a String',
'Write a function that reverses a string. The input string is given as an array
 of characters s.

 You must do this by modifying the input array in-place with O(1) extra memory.

 ### Example 1:

 Input: s = ["h","e","l","l","o"]
 Output: ["o","l","l","e","h"]

 ### Example 2:

 Input: s = ["H","a","n","n","a","h"]
 Output: ["h","a","n","n","a","H"]

 ### Constraints:

 • 1 <= s.length <= 10^5
 • s[i] is a printable ascii character. ',
'Strings, Algorithms', 'Easy'),


(uuid_generate_v4()::VARCHAR, 'Linked List Cycle Detection', 
'Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

 There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail''s `next` pointer is connected to. Note that `pos` is not passed as a parameter.

 Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

 ## Examples

 ### Example 1:

 - Linked List Structure: A sequence of nodes where the 4th node (value -4) points back to the 2nd node (value 2).
 - **Input:** `head = [3,2,0,-4], pos = 1`
 - **Output:** `true`
 - **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

 ### Example 2:

 - Linked List Structure: A sequence of two nodes where the 2nd node (value 2) points back to the 1st node (value 1).
 - **Input:** `head = [1,2], pos = 0`
 - **Output:** `true`
 - **Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

 ### Example 3:

 - Linked List Structure: A single node with no cycle.
 - **Input:** `head = [1], pos = -1`
 - **Output:** `false`
 - **Explanation:** There is no cycle in the linked list.

 ## Constraints

 - The number of the nodes in the list is in the range `[0, 104]`.
 - `-10^5 <= Node.val <= 10^5`
 - `pos` is `-1` or a valid index in the linked-list.

 ## Follow-up

 Can you solve it using `O(1)` (i.e., constant) memory?',
'Data Structures, Algorithms', 'Easy')
;
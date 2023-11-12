/** `localStorage` key for storing questions. */
const QUESTIONS_STORAGE_KEY = 'questions'

/** Represents a question in the question bank. */
export interface Question {
    /** The UUID for the question. */
    id: string
    /** The title of the question. */
    title: string
    /** The description of the question. */
    description: string
    /** Category associated with the question. */
    category: string
    /** The complexity level of the question. */
    complexity: 'Easy' | 'Medium' | 'Hard'
}

/**
 * Generates a UUID similar to that of UUID v4.
 *
 * @private
 * @returns {string} Generated UUID.
 */
function _generateUUID(): string {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
        const r = (Math.random() * 16) | 0
        const v = c === 'x' ? r : (r & 0x3) | 0x8
        return v.toString(16)
    })
}

/**
 * Stores a new question.
 *
 * @param {Omit<Question, 'id'>} question The question to store. All fields except ID are required.
 * @returns {Promise<string>} Resolves with the UUID for the stored question.
 */
export async function storeQuestion(question: Omit<Question, 'id'>): Promise<string> {
    const id = _generateUUID()
    const questions = await getAllQuestions()
    const newQuestion = { id, ...question }

    questions.push(newQuestion)
    localStorage.setItem(QUESTIONS_STORAGE_KEY, JSON.stringify(questions))
    return id
}

/**
 * Retrieves a question by its ID.
 *
 * @param {string} id The ID of the question to retrieve.
 * @returns {Promise<Question>} Resolves with the Question object if found.
 */
export async function getQuestion(id: string): Promise<Question> {
    const questions = await getAllQuestions()
    return questions.find((q) => q.id === id)!
}

/**
 * Retrieves all questions.
 *
 * @returns {Promise<Question[]>} An array of questions.
 */
export async function getAllQuestions(): Promise<Question[]> {
    return JSON.parse(localStorage.getItem(QUESTIONS_STORAGE_KEY) || '[]')
}

/**
 * Updates an existing question by its ID.
 *
 * @param {Pick<Question, 'id'> & Partial<Omit<Question, 'id'>>} updatedQuestion
 * Question with the fields to update. All fields except `id` are optional.
 * @returns {Promise<void>} Resolves when the question is successfully updated.
 */
export async function updateQuestion(
    updatedQuestion: Pick<Question, 'id'> & Partial<Omit<Question, 'id'>>
): Promise<void> {
    const questions: Question[] = await getAllQuestions()
    const index = questions.findIndex((q) => q.id === updatedQuestion.id)

    if (index > -1) {
        questions[index] = { ...questions[index], ...updatedQuestion }
        localStorage.setItem(QUESTIONS_STORAGE_KEY, JSON.stringify(questions))
    }
}

/**
 * Deletes a question by its ID.
 *
 * @param {string} id The ID of the question to be deleted.
 * @returns {Promise<void>} Resolves when the question is successfully deleted.
 */
export async function deleteQuestion(id: string): Promise<void> {
    const questions: Question[] = await getAllQuestions()
    const newQuestions = questions.filter((q) => q.id !== id)
    localStorage.setItem(QUESTIONS_STORAGE_KEY, JSON.stringify(newQuestions))
}

/**
 * Deletes all questions.
 *
 * @returns {Promise<void>} Resolves when all questions are successfully deleted.
 */
export async function deleteAllQuestions(): Promise<void> {
    localStorage.removeItem(QUESTIONS_STORAGE_KEY)
}
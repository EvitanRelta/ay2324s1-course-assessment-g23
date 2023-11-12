import { QuestionTable } from '../components/QuestionTable/QuestionTable.tsx'
import Navbar from '../components/Navbar.tsx'
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import MatchBar from '../components/MatchBar.tsx'
import { useCurrentUser } from '../stores/userStore.ts'

const Questions = () => {
    const { data: user } = useCurrentUser()
    const isUser = user?.role === 'normal'

    const navigate = useNavigate()

    // Redirect if not logged in.
    useEffect(() => {
        const isNotLoggedIn = user === null
        if (isNotLoggedIn) navigate('/')
    }, [user, navigate])

    return (
        <>
            <Navbar />
            <div className='question-page-container'>
                {isUser && <MatchBar />}
                <QuestionTable />
            </div>
        </>
    )
}

export default Questions

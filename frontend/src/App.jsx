import { Navigate, Route, Routes, useParams } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import SubjectPage from "./pages/SubjectPage";
import KnowledgePage from "./pages/KnowledgePage";
import PracticePage from "./pages/PracticePage";
import PaperPage from "./pages/PaperPage";
import QuestionPage from "./pages/QuestionPage";
import MistakesPage from "./pages/MistakesPage";
import ProgressPage from "./pages/ProgressPage";
import AttemptPage from "./pages/AttemptPage";
import SearchPage from "./pages/SearchPage";
import AdminPage from "./pages/AdminPage";
import NotFound from "./pages/NotFound";
import { useGrade } from "./context/GradeContext";

function SubjectRedirect() {
  const { subjectId } = useParams();
  const { gradeId } = useGrade();
  return <Navigate to={`/grades/${gradeId || "8"}/subjects/${subjectId}`} replace />;
}

export default function App() {
  return (
    <>
      <Header />
      <main id="main" className="main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/grades/:gradeId/subjects/:subjectId" element={<SubjectPage />} />
          <Route path="/subjects/:subjectId" element={<SubjectRedirect />} />
          <Route path="/knowledge/:id" element={<KnowledgePage />} />
          <Route path="/practice/:id" element={<PracticePage />} />
          <Route path="/papers/:id" element={<PaperPage />} />
          <Route path="/practice/question/:id" element={<QuestionPage />} />
          <Route path="/questions/:id" element={<QuestionPage />} />
          <Route path="/mistakes" element={<MistakesPage />} />
          <Route path="/progress" element={<ProgressPage />} />
          <Route path="/attempts/:id" element={<AttemptPage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/admin" element={<AdminPage />} />
          <Route path="/code" element={<Navigate to="/" replace />} />
          <Route path="/lab" element={<Navigate to="/" replace />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
      <Footer />
    </>
  );
}

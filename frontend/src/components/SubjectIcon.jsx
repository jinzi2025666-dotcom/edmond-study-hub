const icons = {
  chinese: (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <rect x="5" y="5" width="14" height="14" />
      <path d="M8.5 9.2h7M12 9.2V16M8.8 16h6.4" />
      <path d="M20 12.5 22 19h-9" />
    </g>
  ),
  mathematics: (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round">
      <circle cx="9" cy="15" r="4.2" />
      <path d="M13.2 12.2 19 6.5M17.2 6.5H19V8.4M7.2 15h3.6M9 13.2v3.6" />
    </g>
  ),
  english: (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 7.5c3.2-1.5 5.8-1.5 7 0v11c-1.2-1.4-3.8-1.4-7 0V7.5zM12 7.5c3.2-1.5 5.8-1.5 7 0v11c-1.2-1.4-3.8-1.4-7 0" />
    </g>
  ),
  "computer-science": (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <rect x="4.5" y="6" width="15" height="10.5" />
      <path d="M9 20h6M12 16.5V20M8 10.2l2.2 2.2L8 14.6M16 10.2l-2.2 2.2L16 14.6" />
    </g>
  ),
  economics: (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 19h14M6.5 16.5 10 11l3 4 4.5-8" />
      <circle cx="17.5" cy="7" r="1.2" fill="currentColor" stroke="none" />
    </g>
  ),
  physics: (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M7 19h10M12 19V7.5M8.5 8.2 12 7.5l3.5 0.7" />
      <path d="M12 7.5c3.4 1.2 5.5 3.8 5.5 6.8" />
    </g>
  ),
  chemistry: (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M10 5v6.2L6.8 18.2A2.4 2.4 0 0 0 8.9 21.5h6.2a2.4 2.4 0 0 0 2.1-3.3L14 11.2V5" />
      <path d="M9.5 5h5" />
    </g>
  ),
  biology: (
    <g fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 20V8.5" />
      <path d="M12 16.5c-3-1.2-5-3.4-5-6.2 0-2 1.2-3.3 3.2-3.3 2.5 0 3.6 2.4 3.6 5" />
      <path d="M12 14.5c3-1.1 5-3.2 5-5.8 0-2-1.1-3.2-3-3.2-2.3 0-3.5 2-3.5 4.6" />
    </g>
  ),
};

export default function SubjectIcon({ id, size = 28, title }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" role="img" aria-hidden={title ? undefined : true} aria-label={title}>
      {icons[id] || icons.english}
    </svg>
  );
}

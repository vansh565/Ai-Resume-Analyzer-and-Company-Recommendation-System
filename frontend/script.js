const DOM = {
  resumeInput: document.getElementById('resumeInput'),
  jobDescription: document.getElementById('jobDescription'),
  charCount: document.getElementById('charCount'),
  fileInfo: document.getElementById('fileInfo'),
  fileName: document.getElementById('fileName'),
  removeFile: document.getElementById('removeFile'),
  analyzeBtn: document.getElementById('analyzeBtn'),
  resetBtn: document.getElementById('resetBtn'),
  loading: document.getElementById('loadingContainer'),
  results: document.getElementById('resultsCard'),
  scoreNumber: document.getElementById('scoreNumber'),
  scoreProgress: document.getElementById('scoreProgress'),
  scoreMessage: document.getElementById('scoreMessage'),
  suggestions: document.getElementById('suggestions'),
  skillsContainer: document.getElementById('skillsContainer'),
  parseTreeBox: document.getElementById('parseTreeBox'),
  irBox: document.getElementById('irBox'),
  toggleParseBtn: document.getElementById('toggleParseBtn'),
  toggleIRBtn: document.getElementById('toggleIRBtn'),
  analyzeAgainBtn: document.getElementById('analyzeAgainBtn'),
  companyRecommendations: document.getElementById('companyRecommendations')
};

let uploadedFile = null;

// FILE UPLOAD
DOM.resumeInput.addEventListener("change", e => {
  uploadedFile = e.target.files[0];
  DOM.fileName.textContent = uploadedFile.name;
  DOM.fileInfo.style.display = "flex";
});

// REMOVE FILE
DOM.removeFile?.addEventListener("click", () => {
  uploadedFile = null;
  DOM.resumeInput.value = "";
  DOM.fileInfo.style.display = "none";
});

// CHARACTER COUNT
DOM.jobDescription.addEventListener("input", e => {
  DOM.charCount.textContent = `${e.target.value.length} characters`;
});

// ANALYZE BUTTON
DOM.analyzeBtn.addEventListener("click", async () => {
  if (!uploadedFile || DOM.jobDescription.value.length < 10) {
    alert("Upload resume and enter job description");
    return;
  }

  DOM.loading.style.display = "block";

  const formData = new FormData();
  formData.append("resume", uploadedFile);
  formData.append("job_desc", DOM.jobDescription.value);

  try {
    const res = await fetch("/analyze", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    DOM.loading.style.display = "none";

    console.log("SERVER RESPONSE:", data);

    renderResults(data);

  } catch (error) {
    DOM.loading.style.display = "none";
    alert("Server error: " + error.message);
  }
});

// RENDER RESULTS
function renderResults(data) {
  DOM.results.style.display = "block";

  animateScore(data.ATS_Match_Score || 0);

  DOM.scoreMessage.textContent =
    data.ATS_Match_Score >= 75
      ? "Excellent ATS compatibility 🔥"
      : data.ATS_Match_Score >= 50
      ? "Good match with improvement scope 👍"
      : "Low ATS score. Optimization needed ❗";

  // Add score class for styling
  if (data.ATS_Match_Score >= 75) {
    DOM.scoreMessage.className = "score-message excellent";
  } else if (data.ATS_Match_Score >= 50) {
    DOM.scoreMessage.className = "score-message good";
  } else {
    DOM.scoreMessage.className = "score-message poor";
  }

  // Gemini Feedback
  DOM.suggestions.innerHTML = `
    <div class="suggestion-item">
      <div class="suggestion-icon">📝</div>
      <div class="suggestion-content">
        <div class="suggestion-title">AI Feedback</div>
        <div class="suggestion-description">${formatFeedback(data.Gemini_Feedback || "No feedback received.")}</div>
      </div>
    </div>
  `;

  // Display Extracted Skills
  if (data.Extracted_Skills && data.Extracted_Skills.length > 0) {
    displaySkills(data.Extracted_Skills);
  } else {
    DOM.skillsContainer.innerHTML = '<p class="no-data">No skills extracted</p>';
  }

  // Display Company Recommendations
  if (data.Company_Recommendations && Object.keys(data.Company_Recommendations).length > 0) {
    displayCompanyRecommendations(data.Company_Recommendations);
  } else {
    DOM.companyRecommendations.innerHTML = '<p class="no-data">No company recommendations available</p>';
  }

  // Parse Tree
  DOM.parseTreeBox.textContent = data.Parse_Tree || "No Parse Tree Generated";

  // IR
  DOM.irBox.textContent = data.IR_Code || "No Intermediate Code Generated";
}

// Format feedback text
function formatFeedback(feedback) {
  // Convert markdown-style formatting to HTML
  let formatted = feedback
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>');
  
  return formatted;
}

// Display skills with tags
function displaySkills(skills) {
  DOM.skillsContainer.innerHTML = '';
  
  skills.forEach(skill => {
    const skillTag = document.createElement('div');
    skillTag.className = 'skill-tag';
    skillTag.innerHTML = `
      <span class="skill-icon">✓</span>
      <span>${skill}</span>
    `;
    DOM.skillsContainer.appendChild(skillTag);
  });
}

// Display company recommendations with detailed information
function displayCompanyRecommendations(recommendations) {
  DOM.companyRecommendations.innerHTML = '';
  
  // Check if there are any recommendations
  const hasRecommendations = Object.keys(recommendations).length > 0;
  
  if (!hasRecommendations) {
    DOM.companyRecommendations.innerHTML = `
      <div class="no-recommendations">
        <p>No company recommendations available at this time.</p>
        <p>Try uploading a resume with more specific skills.</p>
      </div>
    `;
    return;
  }
  
  // Loop through categories
  for (const [category, companies] of Object.entries(recommendations)) {
    // Format category name for display
    const categoryName = category.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    
    // Create category header
    const categoryHeader = document.createElement('div');
    categoryHeader.className = 'company-category-header';
    categoryHeader.innerHTML = `
      <h3 class="company-category">${categoryName}</h3>
      <p class="category-description">Top companies hiring for ${categoryName.toLowerCase()} roles</p>
    `;
    DOM.companyRecommendations.appendChild(categoryHeader);
    
    // Create grid for this category
    const categoryGrid = document.createElement('div');
    categoryGrid.className = 'companies-grid';
    
    companies.forEach(company => {
      const card = document.createElement('div');
      card.className = 'company-card-detailed';
      card.innerHTML = `
        <div class="company-header">
          <h4 class="company-name">${escapeHtml(company.name)}</h4>
          <div class="company-rating">
            <span class="rating-stars">★</span>
            <span class="rating-value">${company.rating || 'N/A'}</span>
          </div>
        </div>
        
        <div class="company-details">
          <div class="company-package">
            <span class="detail-icon">💰</span>
            <span class="detail-label">Package:</span>
            <span class="detail-value">${company.package || 'Competitive'}</span>
          </div>
          
          <div class="company-roles">
            <span class="detail-icon">💼</span>
            <span class="detail-label">Key Roles:</span>
            <div class="roles-list">
              ${company.roles ? company.roles.map(role => `<span class="role-tag">${role}</span>`).join('') : 'Various roles available'}
            </div>
          </div>
          
          <div class="company-locations">
            <span class="detail-icon">📍</span>
            <span class="detail-label">Locations:</span>
            <span class="detail-value">${company.locations ? company.locations.join(', ') : 'Multiple locations'}</span>
          </div>
          
          <div class="company-description">
            <span class="detail-icon">ℹ️</span>
            <span class="detail-label">About:</span>
            <p class="description-text">${company.description || 'Leading company in the industry with great opportunities for growth.'}</p>
          </div>
        </div>
        
        <div class="company-actions">
          <a href="${company.link}" target="_blank" rel="noopener noreferrer" class="btn-apply">
            View Opportunities →
          </a>
          <button class="btn-save" onclick="saveCompany('${company.name}')">
            📌 Save
          </button>
        </div>
      `;
      categoryGrid.appendChild(card);
    });
    
    DOM.companyRecommendations.appendChild(categoryGrid);
  }
  
  // Add "View More" section
  const viewMoreSection = document.createElement('div');
  viewMoreSection.className = 'view-more-section';
  viewMoreSection.innerHTML = `
    <button class="btn-view-more" onclick="loadMoreCompanies()">
      🔍 Find More Companies
    </button>
    <p class="view-more-hint">Discover more opportunities based on your skills</p>
  `;
  DOM.companyRecommendations.appendChild(viewMoreSection);
}

// Function to save company for later
function saveCompany(companyName) {
  let savedCompanies = JSON.parse(localStorage.getItem('savedCompanies') || '[]');
  if (!savedCompanies.includes(companyName)) {
    savedCompanies.push(companyName);
    localStorage.setItem('savedCompanies', JSON.stringify(savedCompanies));
    showNotification(`✓ ${companyName} saved to your list!`);
  } else {
    showNotification(`${companyName} is already in your saved list.`);
  }
}

// Function to show notification
function showNotification(message) {
  const notification = document.createElement('div');
  notification.className = 'notification';
  notification.textContent = message;
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.classList.add('show');
  }, 100);
  
  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

// Function to load more companies (can be expanded to fetch from API)
function loadMoreCompanies() {
  showNotification('Finding more opportunities based on your profile...');
  // You can implement API call to fetch more companies here
  setTimeout(() => {
    showNotification('Check back soon for more personalized recommendations!');
  }, 1500);
}

// Helper function to escape HTML
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

// SCORE ANIMATION
function animateScore(score) {
  const circumference = 2 * Math.PI * 90;
  const offset = circumference - (score / 100) * circumference;
  
  if (DOM.scoreProgress) {
    DOM.scoreProgress.style.strokeDashoffset = offset;
    
    // Change color based on score
    if (score >= 75) {
      DOM.scoreProgress.style.stroke = '#10b981';
    } else if (score >= 50) {
      DOM.scoreProgress.style.stroke = '#f59e0b';
    } else {
      DOM.scoreProgress.style.stroke = '#ef4444';
    }
  }

  let current = 0;
  const interval = setInterval(() => {
    DOM.scoreNumber.textContent = current;
    current++;
    if (current > score) clearInterval(interval);
  }, 15);
}

// TOGGLE PARSE TREE
DOM.toggleParseBtn?.addEventListener("click", () => {
  if (DOM.parseTreeBox.style.display === "none") {
    DOM.parseTreeBox.style.display = "block";
  } else {
    DOM.parseTreeBox.style.display = "none";
  }
});

// TOGGLE IR
DOM.toggleIRBtn?.addEventListener("click", () => {
  if (DOM.irBox.style.display === "none") {
    DOM.irBox.style.display = "block";
  } else {
    DOM.irBox.style.display = "none";
  }
});

// ANALYZE AGAIN
DOM.analyzeAgainBtn?.addEventListener("click", () => {
  location.reload();
});

// RESET
DOM.resetBtn.addEventListener("click", () => location.reload());

// CHATBOT FUNCTIONALITY
const chatDOM = {
  messages: document.getElementById('chatMessages'),
  input: document.getElementById('chatInput'),
  sendBtn: document.getElementById('sendChatBtn'),
  container: document.getElementById('chatContainer')
};

function addMessage(text, type = 'bot') {
  const msg = document.createElement('div');
  msg.classList.add('message', type);
  msg.textContent = text;
  chatDOM.messages.appendChild(msg);
  chatDOM.messages.scrollTop = chatDOM.messages.scrollHeight;
}

function addLoading() {
  const loading = document.createElement('div');
  loading.classList.add('message', 'bot', 'loading');
  loading.textContent = "Thinking...";
  loading.id = 'loadingMsg';
  chatDOM.messages.appendChild(loading);
  chatDOM.messages.scrollTop = chatDOM.messages.scrollHeight;
  return loading;
}

function removeLoading(loadingEl) {
  if (loadingEl && loadingEl.parentNode) {
    loadingEl.parentNode.removeChild(loadingEl);
  }
}

async function sendMessage() {
  const message = chatDOM.input.value.trim();
  if (!message) return;

  // Show user message
  addMessage(message, 'user');
  chatDOM.input.value = '';

  // Show loading
  const loading = addLoading();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });

    if (!res.ok) throw new Error('Chat failed');

    const data = await res.json();
    removeLoading(loading);
    addMessage(data.reply || "No response received.");
    
  } catch (err) {
    removeLoading(loading);
    addMessage("Sorry, something went wrong. Try again later.", 'bot');
    console.error(err);
  }
}

// Send on button click
chatDOM.sendBtn.addEventListener('click', sendMessage);

// Send on Enter (without Shift)
chatDOM.input.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// Welcome message when page loads
window.addEventListener('load', () => {
  addMessage("Hi! I'm your resume expert. Ask me anything about ATS, keywords, structure, improvements...", 'bot');
});
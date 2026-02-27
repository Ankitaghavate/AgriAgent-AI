// Optional: Scroll animations using IntersectionObserver
const faders = document.querySelectorAll('.animate__fadeIn, .animate__fadeInLeft, .animate__fadeInRight');

const appearOptions = {
  threshold: 0.2,
  rootMargin: "0px 0px -50px 0px"
};

const appearOnScroll = new IntersectionObserver(function(entries, observer){
    entries.forEach(entry => {
        if(!entry.isIntersecting) return;
        entry.target.classList.add('animate__animated', 'animate__fadeInUp');
        observer.unobserve(entry.target);
    });
}, appearOptions);

faders.forEach(fader => {
    appearOnScroll.observe(fader);
});
const chatbotContainer = document.getElementById('chatbot-container');
const chatbotToggle = document.getElementById('chatbot-toggle');
const chatbotSend = document.getElementById('chatbot-send');
const chatbotInput = document.getElementById('chatbot-input');
const chatbotMessages = document.getElementById('chatbot-messages');

chatbotToggle.addEventListener('click', () => {
    chatbotContainer.style.display = 'none';
});

chatbotSend.addEventListener('click', sendMessage);
chatbotInput.addEventListener('keypress', function(e){
    if(e.key === 'Enter') sendMessage();
});

function appendMessage(sender, text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = sender === 'user' ? 'chatbot-user' : 'chatbot-bot';
    msgDiv.innerHTML = `<span>${text}</span>`;
    chatbotMessages.appendChild(msgDiv);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function sendMessage() {
    const message = chatbotInput.value.trim();
    if(!message) return;

    appendMessage('user', message);
    chatbotInput.value = '';

    fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
    })
    .then(res => res.json())
    .then(data => {
        appendMessage('bot', data.response);
    })
    .catch(err => {
        appendMessage('bot', '⚠️ Error: Could not get response.');
    });
}

// Handle advisory form submission with AJAX
document.addEventListener('DOMContentLoaded', function() {
    const advisoryForm = document.getElementById('advisoryForm');
    const generateBtn = document.getElementById('generateBtn');
    const loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));

    if (advisoryForm) {
        advisoryForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Show loading modal
            loadingModal.show();

            // Disable button
            generateBtn.disabled = true;
            generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';

            // Prepare form data
            const formData = new FormData(this);

            // Send AJAX request
            fetch('/generate_ajax', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Redirect to result page
                    window.location.href = data.redirect_url;
                } else {
                    // Hide loading modal
                    loadingModal.hide();

                    // Re-enable button
                    generateBtn.disabled = false;
                    generateBtn.innerHTML = '<i class="fas fa-file-waveform me-2"></i>Generate Report ✨';

                    // Show error message
                    alert('An error occurred. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);

                // Hide loading modal
                loadingModal.hide();

                // Re-enable button
                generateBtn.disabled = false;
                generateBtn.innerHTML = '<i class="fas fa-file-waveform me-2"></i>Generate Report ✨';

                // Show error message
                alert('An error occurred. Please try again.');
            });
        });
    }
});


document.getElementById("advisoryForm").addEventListener("submit", async function(e) {
    e.preventDefault(); // prevent page reload
    const generateBtn = document.getElementById("generateBtn");
    generateBtn.disabled = true;
    generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Generating...';

    // Collect form data
    const formData = {
        crop_type: document.getElementById("crop_type").value,
        state: document.getElementById("state").value,
        land_size: document.getElementById("land_size").value,
        income_level: document.getElementById("income_level").value,
        farming_type: document.getElementById("farming_type").value
    };

    try {
        const res = await fetch("/generate_report", {  // Flask route we will create
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(formData)
        });
        const data = await res.json();

        // Show the report
        const reportDiv = document.getElementById("reportResult");
        const reportContent = document.getElementById("reportContent");
        reportContent.textContent = data.report; // server returns JSON {report: "..."}
        reportDiv.classList.remove("d-none");

    } catch (err) {
        alert("Error generating report: " + err.message);
    } finally {
        generateBtn.disabled = false;
        generateBtn.innerHTML = '<i class="fas fa-file-waveform me-2"></i>Generate Report ✨';
    }
});
document.getElementById('advisoryForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Show loading modal
    var loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
    loadingModal.show();

    // Collect form data
    const formData = {
        crop_type: document.getElementById('crop_type').value,
        state: document.getElementById('state').value,
        land_size: document.getElementById('land_size').value,
        income_level: document.getElementById('income_level').value,
        farming_type: document.getElementById('farming_type').value
    };

    try {
        // Call your backend API for generating the report
        const response = await fetch('/generate_report', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        // Hide loading modal
        loadingModal.hide();

        // Show report (you can use a modal, alert, or render on the page)
        alert('Report Generated: ' + JSON.stringify(result));

    } catch (error) {
        loadingModal.hide();
        alert('Error generating report. Please try again.');
        console.error(error);
    }
});
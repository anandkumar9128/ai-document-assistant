css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

body {
    font-family: 'Inter', sans-serif;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.chat-message {
    padding: 1.2rem;
    border-radius: 12px;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: flex-start;
    animation: fadeIn 0.4s ease-out forwards;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    line-height: 1.6;
}

.chat-message.user {
    background: linear-gradient(135deg, #1e2532 0%, #151a23 100%);
    border: 1px solid #2d3748;
}

.chat-message.bot {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.chat-message .avatar {
  width: 45px;
  height: 45px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  overflow: hidden;
  background-color: #2b313e;
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.chat-message .avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.chat-message .message {
  width: 100%;
  padding: 0 1.2rem;
  color: #e2e8f0;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://api.dicebear.com/7.x/bottts/svg?seed=Gemini&backgroundColor=333333" alt="AI">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix&backgroundColor=333333" alt="User">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Продвинутый редактор презентаций</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Roboto+Mono&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #4A90E2;
            --secondary: #50E3C2;
            --background: #f5f6fa;
            --text: #2d3436;
        }

        /* Базовые стили */
        body {
            margin: 0;
            padding: 20px;
            font-family: 'Montserrat', sans-serif;
            background: var(--background);
            color: var(--text);
            transition: 0.3s all;
        }

        /* Контейнер редактора */
        .editor {
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 30px;
            height: 95vh;
        }

        /* Панель управления */
        .controls {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        /* Область просмотра */
        .preview {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }

        /* Слайд */
        .slide {
            width: 100%;
            height: 100%;
            min-height: 500px;
            background: white;
            border-radius: 12px;
            padding: 40px;
            position: relative;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: 0.3s all;
        }

        /* Стили для кнопок */
        .btn {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border: none;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: 0.3s all;
            display: flex;
            align-items: center;
            gap: 8px;
            margin: 10px 0;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(74,144,226,0.3);
        }

        .btn-icon {
            font-size: 1.2em;
        }

        /* Поля ввода */
        input[type="text"], input[type="color"] {
            width: 100%;
            padding: 12px;
            border: 2px solid #eee;
            border-radius: 8px;
            margin: 10px 0;
            transition: 0.3s all;
        }

        input[type="text"]:focus {
            border-color: var(--primary);
            outline: none;
        }

        /* Медиа контент */
        .media-container {
            max-width: 80%;
            margin: 20px auto;
            border-radius: 12px;
            overflow: hidden;
            transition: 0.3s all;
        }

        /* Анимации */
        @keyframes slideIn {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        /* Темная тема */
        .dark-mode {
            --background: #2d3436;
            --text: #f5f6fa;
        }
    </style>
</head>
<body>
    <div class="editor">
        <!-- Панель управления -->
        <div class="controls">
            <h2>🎨 Редактор презентаций</h2>
            
            <button class="btn" onclick="addSlide()">
                <span class="btn-icon">➕</span> Новый слайд
            </button>
            
            <button class="btn" onclick="deleteSlide()" style="background: linear-gradient(135deg, #ff7675, #d63031)">
                <span class="btn-icon">🗑</span> Удалить слайд
            </button>

            <div class="settings-section">
                <h3>🎨 Дизайн слайда</h3>
                <input type="color" id="bgColor">
                <input type="text" id="bgImage" placeholder="🌄 URL фонового изображения...">
                <button class="btn" onclick="applyBackground()">
                    <span class="btn-icon">🎨</span> Применить фон
                </button>
            </div>

            <div class="settings-section">
                <h3>🖼 Медиа контент</h3>
                <input type="text" id="imageUrl" placeholder="📷 URL изображения...">
                <button class="btn" onclick="addImage()">
                    <span class="btn-icon">🖼</span> Добавить фото
                </button>
                
                <input type="text" id="videoUrl" placeholder="🎥 URL видео...">
                <button class="btn" onclick="addVideo()">
                    <span class="btn-icon">🎥</span> Добавить видео
                </button>
            </div>

            <div class="settings-section">
                <h3>💾 Экспорт</h3>
                <button class="btn" onclick="savePresentation()" style="background: linear-gradient(135deg, #00b894, #55efc4)">
                    <span class="btn-icon">💾</span> Сохранить презентацию
                </button>
            </div>
        </div>

        <!-- Область просмотра -->
        <div class="preview" id="preview">
            <div class="slide active" id="currentSlide">
                <h2 contenteditable="true" style="color: var(--primary)">Заголовок слайда</h2>
                <p contenteditable="true">Начните редактировать текст...</p>
            </div>
        </div>
    </div>

    <script>
        // ... (оставить JavaScript из предыдущей версии без изменений)
        // (Тот же самый JavaScript код что и в предыдущем примере)
    </script>
</body>
</html>

import os
import sys

# Añadir tanto src como examples al path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, 'src'))
sys.path.append(os.path.join(project_root, 'examples'))

# Ahora importar
from complete_pipeline import process_complete

# Usar el proceso
summary = process_complete(
    video_url="https://www.youtube.com/watch?v=tu_video",
    output_dir="output",
    model_players_path="models/players/best.pt",
    model_ball_path="models/ball/best.pt",
    device="mps",
    start_time="01:30:00",
    duration="00:05:00"
)
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from simulate import MetabolicEnvironment, LiverMetabolismSystem
from vis import generate_interactive_dashboard

if __name__ == "__main__":
    # Create output directory
    os.makedirs("../results-html", exist_ok=True)
    
    # Initialize environment
    env = MetabolicEnvironment()
    
    # Set ALDH activity to extremely low (e.g. 10%)
    # This simulates ALDH deficiency (Asian Flush / toxic acetaldehyde accumulation)
    env.setParameter("aldh_activity", 0.1)
    
    def inject(e: MetabolicEnvironment, t: int):
        # Simulate alcohol intake between 10 and 20 minutes
        if 10 <= t <= 15:
            e.setMetabolite("ethanol", e.getMetabolite("ethanol") + 0.5) 
            
    system = LiverMetabolismSystem(env)
    minutes = 60 * 8
    
    print("Starting simulation with Low ALDH Activity (0.1)...")
    for tt in range(minutes):
        hour = tt / 60.0
        inject(env, tt)
        system.step(hour)
        
    output_file = "../results-html/interactive_alcohol_low_aldh.html"
    generate_interactive_dashboard(env.history, filename=output_file)
    print(f"Simulation complete. Results saved to {output_file}")

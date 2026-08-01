# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TimeBox
import time as _time

class TimeBoxUndo:
    def __init__(self, last_action):
        self.last_action = last_action
    
    def undo(self, current_state):
        return self._revert(current_state)
    
    def _revert(self, state):
        if isinstance(state, TaskState):
            state.status = 'planned'
            state.completed_at = None
        
        elif isinstance(state, TimedBoxState):
            state.is_active = True
            state.current_task = self.last_action.get('current_task', None)
        
        elif isinstance(state, BreakState):
            state.is_active = False
        
        elif isinstance(state, Statistics):
            if 'completed' in state:
                completed_list = [s for s in state.completed.values() if s]
                total_completed = sum(completed_list)
                state.total_completed = total_completed
                state.total_sessions = 0

        return state

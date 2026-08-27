# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: TimeBox
def test_timer():
    from timebox import Timer
    t = Timer(5)
    assert t.remaining() == 5
    assert t.is_running() == False
    t.start()
    assert t.is_running() == True
    assert 0 < t.remaining() < 5
    t.stop()
    assert t.is_running() == False
    assert t.remaining() == 0
    assert t.elapsed() > 0

def test_task():
    from timebox import Task
    t = Task("read", "30m")
    assert t.name == "read"
    assert t.duration == 1800
    assert t.is_done() == False
    t.mark_done()
    assert t.is_done() == True

def test_day():
    from timebox import Day
    d = Day("Mon")
    assert d.name == "Mon"
    d.add_task("read", "30m")
    assert len(d.tasks) == 1
    d.add_break("10m")
    assert len(d.breaks) == 1
    d.add_task("code", "2h")
    assert len(d.tasks) == 2
    d.mark_done("read")
    assert len(d.tasks) == 1
    assert d.tasks[0].name == "code"

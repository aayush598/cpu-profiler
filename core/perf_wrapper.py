import subprocess

def run_perf(code_snippet, events=None):
    if events is None:
        events = ['cycles', 'instructions', 'cache-misses']

    command = [
        'perf', 'stat',
        '-e', ','.join(events),
        '--', 'python3', '-c', code_snippet
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stderr.decode()  # perf outputs to stderr

run:
	make median_tracker

median_tracker:
	ipython3 median_tracker.py

clean:
	rm -f *.pyc *.pyo
	rm -rf __pycache__/

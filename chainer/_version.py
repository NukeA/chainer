__version__ = '6.0.0a1'


_optional_dependencies = [
    {
        'name': 'CuPy',
        'packages': [
            'cupy-cuda92',
            'cupy-cuda91',
            'cupy-cuda90',
            'cupy-cuda80',
            'cupy',
        ],
        'specifier': '==6.0.0a1',
        'help': 'https://docs-cupy.chainer.org/en/latest/install.html',
    },
    {
        'name': 'iDeep',
        'packages': [
            'ideep4py',
        ],
        'specifier': '>=2.0, <2.1',
        'help': 'https://docs.chainer.org/en/latest/tips.html',
    },
]

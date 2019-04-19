# -*- generated by 1.0.12 -*-
import da
PatternExpr_183 = da.pat.TuplePattern([da.pat.ConstantPattern('Election'), da.pat.FreePattern('p')])
PatternExpr_208 = da.pat.TuplePattern([da.pat.ConstantPattern('Election'), da.pat.SelfPattern()])
PatternExpr_245 = da.pat.TuplePattern([da.pat.ConstantPattern('Leader'), da.pat.FreePattern('leader')])
PatternExpr_277 = da.pat.TuplePattern([da.pat.ConstantPattern('Leader'), da.pat.FreePattern(None)])
PatternExpr_215 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Election'), da.pat.SelfPattern()])])
_config_object = {}
import sys

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PSentEvent_1 = []
        self._PReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_183, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_182]), da.pat.EventPattern(da.pat.SentEvent, '_PSentEvent_1', PatternExpr_208, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_245, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_244]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_277, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, left, **rest_363):
        super().setup(left=left, **rest_363)
        self._state.left = left
        self._state.leaderid = None

    def run(self):
        self.initiate()
        self.output('YO from ', self._id)
        super()._label('_st_label_274', block=False)

        def ExistentialOpExpr_275():
            for (_, _, (_ConstantPattern291_, _)) in self._PReceivedEvent_3:
                if (_ConstantPattern291_ == 'Leader'):
                    if True:
                        return True
            return False
        _st_label_274 = 0
        while (_st_label_274 == 0):
            _st_label_274 += 1
            if ExistentialOpExpr_275():
                _st_label_274 += 1
            else:
                super()._label('_st_label_274', block=True)
                _st_label_274 -= 1
        self.output('Done! from ', self._id)
        self.output('Leader is', self._state.leaderid)

    def initiate(self):
        self.send(('Election', self._id), to=self._state.left)

    def _P_handler_182(self, p):
        if (p > self._id):
            self.send(('Election', p), to=self._state.left)
        if (p < self._id):
            if (not PatternExpr_215.match_iter(self._PSentEvent_1, SELF_ID=self._id)):
                self.send(('Election', self._id), to=self._state.left)
        if (p == self._id):
            self.send(('Leader', self._id), to=self._state.left)
    _P_handler_182._labels = None
    _P_handler_182._notlabels = None

    def _P_handler_244(self, leader):
        self._state.leaderid = leader
        if (not (leader == self._id)):
            self.send(('Leader', leader), to=self._state.left)
    _P_handler_244._labels = None
    _P_handler_244._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])
    _config_object = {'channel': 'fifo'}

    def run(self):
        n = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
        ps = list(self.new(P, num=n))
        for (i, p) in enumerate(ps):
            self._setup({p}, (ps[((i + 1) if (i < (len(ps) - 1)) else 0)],))
        self._start(ps)

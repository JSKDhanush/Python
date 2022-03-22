def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:     
        if (sx==tx and sy>ty) or (sy==ty and sx>tx):
            return False
        while sx<ty and sy<tx:
            if ty>tx:
                ty=ty%tx
            else:
                tx=tx%ty
        return (sx==tx and (ty-sy)%sx==0) or (sy==ty and (tx-sx)%sy==0)

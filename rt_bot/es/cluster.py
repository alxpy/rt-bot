from elasticmagic import Cluster
from elasticmagic.result import BulkResult
from elasticmagic.result import SearchResult
from elasticmagic.util import clean_params


class AIOCluster(Cluster):

    async def search(
        self, q, index=None, doc_type=None, routing=None, preference=None,
        timeout=None, search_type=None, query_cache=None,
        terminate_after=None, scroll=None, **kwargs
    ):
        params = clean_params(
            dict({
                'index': index, 'doc_type': doc_type,
                'routing': routing, 'preference': preference,
                'timeout': timeout, 'search_type': search_type,
                'query_cache': query_cache, 'terminate_after': terminate_after,
                'scroll': scroll,
            }, **kwargs)
        )
        raw_result = await self._client.search(body=q.to_dict(), **params)
        return SearchResult(
            raw_result, q._aggregations,
            doc_cls=q._get_doc_cls(), instance_mapper=q._instance_mapper,
        )

    async def bulk(
        self, actions, index=None, doc_type=None, refresh=None,
        timeout=None, consistency=None, replication=None, **kwargs
    ):
        params = clean_params({
            'index': index,
            'doc_type': doc_type,
            'refresh': refresh,
            'timeout': timeout,
            'consistency': consistency,
            'replication': replication,
        }, **kwargs)
        body = []
        for act in actions:
            body.append({act.__action_name__: act.get_meta()})
            source = act.get_source()
            if source is not None:
                body.append(source)
        raw_result = await self._client.bulk(body=body, **params)
        return BulkResult(raw_result)

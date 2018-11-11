from config.elastic_search import es
from django.conf import settings


class ESMetaClass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'ESModel':
            return type.__new__(cls, name, bases, attrs)
        name = name.lower()
        attrs['__doc_type__'] = name
        cls.__doc_type__ = name
        _class = type.__new__(cls, name, bases, attrs)
        _class.__doc_type__ = name
        return _class


class ESModel(object, metaclass=ESMetaClass):

    def delete(self):
        es.delete(index=settings.ES_INDEX, doc_type=self.__doc_type__, id=self.id)
        return None

    def save(self):
        es.index(index=settings.ES_INDEX, id=self.id, doc_type=self.__doc_type__, body=self.__dict__)
        return self

    @classmethod
    def get(cls, id):
        res = es.get(index=settings.ES_INDEX, doc_type=cls.__doc_type__, id=id)
        return cls(**res['_source'])

    @classmethod
    def filter(cls, **kwargs):
        sort = kwargs.pop('sort')
        res = es.search(
            index=settings.ES_INDEX,
            doc_type=cls.__doc_type__,
            body={"query": {"term": kwargs}, "sort": sort})['hits']['hits']
        
        return [cls(**item['_source']) for item in res]

    @classmethod
    def destroy(cls, id):
        es.delete(index=settings.ES_INDEX, doc_type=cls.__doc_type__, id=id)
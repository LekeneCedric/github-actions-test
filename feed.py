import yaml
import xml.etree.ElementTree as ET


with open('feed.yml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)
    # print(yaml_data)
    # exit(1)
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    for key in ["title", "description", "language", "author"]:
        ET.SubElement(channel, key).text = yaml_data[key]
    
    episodes = ET.SubElement(channel, "episodes")
    for item in yaml_data['episodes']:
        episode = ET.SubElement(episodes, "episode")
        for key in ['title', 'episode_number', 'description', 'release_date', 'duration', 'audio_url', 'transcript_url', 'tags']:
            if key == 'tags':
                tags = ET.SubElement(episode, 'tags')
                for tag in item['tags']:
                    ET.SubElement(tags, 'tag').text = tag
                continue
            if key == 'audio_url':
                ET.SubElement(episode, "enclosure", url=item['audio_url'], type="audio/mpeg")
                continue
            ET.SubElement(episode, key).text = str(item[key])
    
    tree = ET.ElementTree(rss)
    ET.indent(tree, space=" ")
    tree.write('feed.xml', encoding='utf-8', xml_declaration=True)